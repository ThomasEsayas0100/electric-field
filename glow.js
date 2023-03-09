const canvas = document.getElementById('glowingCanvas');
const ctx = canvas.getContext('2d');

const img = new Image();
img.onload = function() {
  canvas.width = img.width;
  canvas.height = img.height;
  ctx.drawImage(img, 500, 0);

  // Create a glowing effect around the canvas
  const imageData = ctx.getImageData(0, 0, canvas.width, canvas.height);
  const data = imageData.data;
  for (let i = 0; i < data.length; i += 4) {
    const r = data[i];
    const g = data[i + 1];
    const b = data[i + 2];
    const alpha = data[i + 3];

    // Set the color to a semi-transparent version of the original color
    data[i] = r;
    data[i + 1] = g;
    data[i + 2] = b;
    data[i + 3] = alpha / 2;
  }
  ctx.putImageData(imageData, 0, 0);
};
img.src = 'heatmap.png';
