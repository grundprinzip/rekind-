var all_files = [];

function setup()
{
    var target = document.getElementById("dropbox");
    target.addEventListener("drop", dropHandler);

    target.addEventListener("dragenter", function(event) {
	event.preventDefault();
	return true;
    });
    target.addEventListener("dragover", function(event) {
	event.preventDefault();
	return true;
    });
}


function dropHandler(event)
{
    try {
	var cont = $("dropbox");
	var fidlist = $("fidlist");
	for (var i = 0; i < event.dataTransfer.files.length; i++)
	{
	    //Titanium.API.log("Processing file: ", event.dataTransfer.files[i]);
	    var fid = event.dataTransfer.files[i];

	    $A(all_files).push(fid);

	    var elem = new Element("li");
	    elem.innerHTML = fid.fileName;
	    cont.appendChild(elem);
	}
    } catch(e){
	Titanium.API.log(e);
    }

}

function processHandler(event)
{
    
}