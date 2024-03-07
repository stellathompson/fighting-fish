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


// Text you want to type out
const typingText = `Welcome to Election Data Visualizer,
your ultimate resource for exploring the
2016 and 2020 elections. Discover the diverse
voting patterns of your specific county along with
information regarding different demographics, race,
and candidates. Whether you're a political enthusiast, researcher, 
or simply curious, our platform offers insightful 
analyses to understand the dynamics of past elections 
like never before. Explore, compare, and gain valuable 
insights about your county by selecting your state
and county down below.<br><br><br>`;

let i = 0;
const speed = 50; // Speed in milliseconds

function typeWriter() {
  if (i < typingText.length) {
    document.getElementById("typeText").innerHTML += typingText.charAt(i);
    i++;
    setTimeout(typeWriter, speed);
  }
}

// Call typeWriter() when the DOM is fully loaded
document.addEventListener("DOMContentLoaded", typeWriter);

