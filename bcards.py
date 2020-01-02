'''Script to download reference business cards images.'''
import requests
import concurrent.futures

SITE = 'https://web.cs.wpi.edu/~claypool/mmsys-dataset/2011/stanford/mvs_images/'


def download_img(img_link):
    '''Downloads images and returns success message.'''
    r = requests.get(SITE + img_link)
    img_name = img_link.split('/')[-1]  # get image name

    with open(f'images/{img_name}', 'wb') as f:  # write file
        f.write(r.content)

    return f'{img_link} downloaded!'


def main():
    '''Driver function.'''
    # generate image links
    ref_bcard_imgs = tuple(
        'business_cards/Reference/{:0>3d}.jpg'.format(x + 1) for x in range(100)
    )

    # multi-threaded downloading
    with concurrent.futures.ThreadPoolExecutor() as executor:
        results = executor.map(download_img, ref_bcard_imgs)

        for result in results:
            print(result)


if __name__ == '__main__':
    main()
