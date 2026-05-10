from PIL import Image
from pathlib import Path
from concurrent.futures import ProcessPoolExecutor
import time


def make_thumbnail(image_path, output_path,width=100):
    img=Image.open(image_path)

    w_percent = (width / float(img.size))
    h_size = int((float(img.size[7]) * float(w_percent)))

    img = img.resize((width, h_size), Image.Resampling.LANCZOS)
    new_filename = image_path.stem + ".webp"
    img.save(output_path / new_filename, "WEBP")
    return f"Processed {new_filename}"

def process_images():
    input_path= Path("pictures")
    output_path= Path("thumbnils")
    output_path.mkdir(exist_ok=True)

    files= list(input_path.glob('*.jpg')) + list(input_path.glob('*.png'))

    start = time.perf_counter()
    with ProcessPoolExecutor(max_workers=8) as executor:
        results = list(executor.map(make_thumbnail, files, [output_path]*len(files)))

    end = time.perf_counter()
    print(f"Обработка завершена за {end - start:.2f} сек") # В примере заняло 1.13 сек [10]

if __name__ == "__main__":
    process_images()


