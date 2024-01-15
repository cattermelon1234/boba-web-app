function demo() {
  const button = document.getElementById("testbutton").textContent = "new text";
}

const apiUrl = 'http://localhost:8000/events';
const outputElement1 = document.getElementById('output1');

function submit() {
  const apiUrl = 'http://localhost:8000/events';
  var name = document.getElementById("textInput").value;

  var title = document.getElementById("textInput2").value;

  var text = document.getElementById("textInput3").value;

  fetch("http://localhost:8000/events", {
    method: "POST",
    body: JSON.stringify({
      name: name,
      title: title,
      text: text
    }),
    headers: {
      "Content-type": "application/json; charset=UTF-8",
      mode: 'no-cors'
    }
  });

  fetch(apiUrl)
  .then(response => {
    console.log("checking");
    //console.log(JSON.parse(response));
    if (!response.ok) {
      throw new Error('Network response was not ok');
    }
    return response.json();
  })
  .then(data => {
    console.log("made it to data!");

    let dataMap = data.map((object) => {
      console.log("updated!");
      const {name, title, text} = object;

      return `
      <div class="container" style="background-color:rgba(114, 88, 70, 0.771); border-width:3px; border-style:solid; border-color:black; margin-bottom: 10px">
        <p style="color:black">Name: ${name}</p>
        <p style="color:black">Title: ${title}</p>
        <p style="color:black">${text}</p> 
      </div>
      `
    }).join("");

    outputElement1.innerHTML = dataMap;

    // Display data in an HTML element
    //console.log("fetched");
    //const obj = JSON.parse(response);
    //for (let i = 0; i < 2; i++) {
      //outputElement1.textContent = data[i].name;
      //outputElement2.textContent = data[i].title;
      //outputElement3.textContent = data[i].text;
    //}
    //outputElement.textContent = JSON.stringify(data, null, 2);
  })
  .catch(error => {
    console.error('Error:', error);
  });

}

fetch(apiUrl)
  .then(response => {
    console.log("checking");
    //console.log(JSON.parse(response));
    if (!response.ok) {
      throw new Error('Network response was not ok');
    }
    return response.json();
  })
  .then(data => {
    console.log("made it to data!");

    let dataMap = data.map((object) => {
      console.log("updated!");
      const {name, title, text} = object;

      return `
      <div class="container" style="background-color:rgba(114, 88, 70, 0.771); border-width:3px; border-style:solid; border-color:black; margin-bottom: 10px">
        <p style="color:black">Name: ${name}</p>
        <p style="color:black">Title: ${title}</p>
        <p style="color:black">${text}</p> 
      </div>
      `
    }).join("");

    outputElement1.innerHTML = dataMap;

    // Display data in an HTML element
    //console.log("fetched");
    //const obj = JSON.parse(response);
    //for (let i = 0; i < 2; i++) {
      //outputElement1.textContent = data[i].name;
      //outputElement2.textContent = data[i].title;
      //outputElement3.textContent = data[i].text;
    //}
    //outputElement.textContent = JSON.stringify(data, null, 2);
  })
  .catch(error => {
    console.error('Error:', error);
  });