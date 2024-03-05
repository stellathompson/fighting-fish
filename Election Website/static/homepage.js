/*
 * webapp.js
 * Yeseo Jeon, Stella Thompson, Kritika Pandit, Luha Yang, Daniel Lumbu
 * March 4, 2024
 *
 * Javascript for the homepage of the web app Election Data Visualizer.
 */


function surprise() {
  the_surprise = document.getElementById("BodyColor");
  the_surprise.style.color = "PaleVioletRed";
  the_surprise.style.fontSize = "60px";
  the_surprise.style.fontWeight = "bold";
}

function changeSizeAndColor() {
  console.log("Mouse over title!");
  the_Title = document.getElementById("Move");
  the_Title.style.backgroundColor = "RoyalBlue";
  the_Title.style.fontSize = "60px";
  the_Title.style.color = "White";
}