var Videos = [];
var Current = 0;

function Next(){
	//Every 60 seconds change current playing video.
	var VideoBox = document.getElementById("Showcase");
	
	if(Current < Videos.length){
		Current ++;
		VideoBox.src = Videos[Current];
	}
}

function SetDelay(){
	console.log("Function set!");
	Timer = setInterval(Next,60000);
}