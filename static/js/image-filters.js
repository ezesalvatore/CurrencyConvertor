// Simple image filter functions
let currentFilter = 'original';

function resetImage() {
    const img = document.getElementById('currencyImage');
    const canvas = document.getElementById('imageCanvas');
    
    currentFilter = 'original';
    img.style.display = 'block';
    canvas.style.display = 'none';
}

function applyFilter(filterFunction) {
    const img = document.getElementById('currencyImage');
    const canvas = document.getElementById('imageCanvas');
    const ctx = canvas.getContext('2d');
    
    canvas.width = img.naturalWidth;
    canvas.height = img.naturalHeight;
    
    ctx.drawImage(img, 0, 0);
    
    const imageData = ctx.getImageData(0, 0, canvas.width, canvas.height);
    const data = imageData.data;
    
    filterFunction(data);
    
    ctx.putImageData(imageData, 0, 0);
    
    img.style.display = 'none';
    canvas.style.display = 'block';
    canvas.className = 'currency-image';
}

function applyGrayscale() {
    currentFilter = 'grayscale';
    applyFilter(function(data) {
        for (let i = 0; i < data.length; i += 4) {
            const gray = Math.floor(0.299 * data[i] + 0.587 * data[i+1] + 0.114 * data[i+2]);
            data[i] = gray;     
            data[i+1] = gray;   
            data[i+2] = gray;   
        }
    });
}

function applySepia() {
    currentFilter = 'sepia';
    applyFilter(function(data) {
        for (let i = 0; i < data.length; i += 4) {
            const r = data[i];
            const g = data[i+1];
            const b = data[i+2];
            
            data[i] = Math.min(255, Math.floor(r * 0.393 + g * 0.769 + b * 0.189));
            data[i+1] = Math.min(255, Math.floor(r * 0.349 + g * 0.686 + b * 0.168));
            data[i+2] = Math.min(255, Math.floor(r * 0.272 + g * 0.534 + b * 0.131));
        }
    });
}

function applyNegative() {
    currentFilter = 'negative';
    applyFilter(function(data) {
        for (let i = 0; i < data.length; i += 4) {
            data[i] = 255 - data[i];      
            data[i+1] = 255 - data[i+1];   
            data[i+2] = 255 - data[i+2];   
        }
    });
}