// get the image container
const imageContainer = document.querySelector('#image-container')
const urls = JSON.parse(imageUrls)

const loadImages = async () => {
    const imagePromises = urls.map(async (url) => {
        const response = await fetch(url);
        const blob = await response.blob();
        const imageUrl = URL.createObjectURL(blob);
        return imageUrl;
    });

    const imageElements = await Promise.all(imagePromises);

    imageElements.forEach((imageUrl) => {
        const img = new Image();
        img.src = imageUrl;
        imageContainer.appendChild(img);
    });
}

loadImages()