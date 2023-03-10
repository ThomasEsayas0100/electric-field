var background_canvas = document.getElementById("backgroundCanvas");
var background_ctx = background_canvas.getContext("2d");
var foreground_canvas = document.getElementById("foregroundCanvas");
var foreground_ctx = foreground_canvas.getContext("2d");

let mouseX, mouseY;
let isMouseDown = false;

document.addEventListener('mousemove', function(event) {
  mouseX = event.offsetX;
  mouseY = event.offsetY;
});

document.addEventListener('mousedown', function(event) {
  isMouseDown = true;
});

document.addEventListener('mouseup', function(event) {
  isMouseDown = false;
});

function sleep(ms) {
  return new Promise(resolve => setTimeout(resolve, ms));
}

function draw_arrow(array) {
  const [start_pos, end_pos, point_a, point_b] = array;

  // set line properties
  background_ctx.beginPath();
  background_ctx.lineWidth = 1;
  background_ctx.strokeStyle = "black";

  // draw line
  background_ctx.moveTo(...start_pos);
  background_ctx.lineTo(...end_pos);
  background_ctx.stroke();

  background_ctx.moveTo(...point_a);
  background_ctx.lineTo(...end_pos);
  background_ctx.stroke();

  background_ctx.moveTo(...point_b);
  background_ctx.lineTo(...end_pos);
  background_ctx.stroke();
}

function draw_circle(coord, radius, ctx) {
  ctx.fillStyle = "#000000";
  ctx.beginPath();
  ctx.arc(coord[0], coord[1], radius, 0, 2 * Math.PI);
  ctx.fill();
  //ctx.stroke();
}



function draw_arrows() {
  fetch('/api/get_arrow')
    .then(response => response.json())
    .then(function(data) {
      for (coords of data)
        draw_arrow(coords);
  });
}

function draw_point_charges(){
  fetch('/api/get_point_charges')
    .then(response => response.json())
    .then(function(data) {
      for (point of data)
        draw_circle(point, 10, background_ctx);
      return data
  });
}

function draw_test_charges() {
  fetch('/api/get_test_charges')
    .then(response => response.json())
    .then(function(data) {
      for (point of data)
        draw_circle(point, 5, foreground_ctx);
  });
}

function draw_background() {
  var img = new Image();
  img.src = "/heatmap.png";

  img.onload = function() {
    background_ctx.drawImage(img, 0, 0);
    draw_arrows()
    draw_point_charges()
  };
  img.onerror = function() {
    console.error('Error loading image');
  };
}
  
draw_background()

 function update_background() {
  fetch('/api/get_point_charges')
    .then(response => response.json())
    .then(function(data) {
      for (point of data)
        point_charge_data = data;
        console.log(point_charge_data);
        for (point of point_charge_data) {
          if (Math.abs(mouseX - point[0]) <= 20) {
            if (Math.abs(mouseY - point[1]) <= 20) {
              if (isMouseDown){
                fetch('/api/update_point_charges', {
                  method: 'POST',
                  headers: {
                    'Content-Type': 'application/json'
                  },
                  body: JSON.stringify([mouseX, mouseY])
                })
                .then(response => response.json())
                .then(function(data) {
                  console.log("Success")
                })
                .catch((error) => {
                  console.error('Error:', error);
                });
                background_ctx.clearRect(0, 0, background_canvas.width, background_canvas.height);
                draw_background()
                draw_point_charges()
                draw_arrows()                                          
              }
            }
          }
        }
  });
}

function move_test_charges () {
  update_background()
  draw_test_charges()
  fetch('/api/update_test_charges')
  requestAnimationFrame(move_test_charges);
}
requestAnimationFrame(move_test_charges);