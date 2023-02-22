function draw_arrow(array) {
  const [start_pos, end_pos, point_a, point_b] = array;
  const canvas = document.getElementById("myCanvas");
  const ctx = canvas.getContext("2d");

  // set line properties
  ctx.beginPath();
  ctx.lineWidth = 1;
  ctx.strokeStyle = "red";

  // draw line
  ctx.moveTo(...start_pos);
  ctx.lineTo(...end_pos);
  ctx.stroke();
}

function draw_circle(coord, radius) {
  const canvas = document.getElementById("myCanvas");
  const ctx = canvas.getContext("2d");
  
  ctx.fillStyle = "#000000";
  ctx.beginPath();
  ctx.arc(coord[0], coord[1], radius, 0, 2 * Math.PI);
  ctx.fill();
  //ctx.stroke();
}
console.log("1")


fetch('/api/get_arrow')
  .then(response => response.json())
  .then(function(data) {
    console.log("data" + data.result);
    for (coords of data)
      draw_arrow(coords);
});

fetch('/api/get_point_charges')
  .then(response => response.json())
  .then(function(data) {
    console.log("data" + data.result);
    for (point of data)
      draw_circle(point, 10);
});

fetch('/api/get_test_charges')
  .then(response => response.json())
  .then(function(data) {
    console.log("data" + data.result);
    for (point of data)
      draw_circle(point, 5);
});