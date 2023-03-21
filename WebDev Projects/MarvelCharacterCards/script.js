function blurelse() {
    document.getElementById('blur3').style = "filter:blur(0px)"
    document.getElementsByTagName('div').style = "filter:blur(3px)"
    console.log('hi');
    document.getElementById('blur3').style = "filter:blur(0px)"
}

function normal() {
    document.body.style = "filter:blur(0px)"
    console.log('hi');
}