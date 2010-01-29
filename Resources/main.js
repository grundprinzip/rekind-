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

    $("action").addEventListener("click", bridgeHandler);
    $("logb").addEventListener("click", function(e){
	$("log").setStyle("display:block;");
	var w = Titanium.UI.currentWindow;
	var h = w.getHeight() + 120;

	// Increase the size
	Titanium.API.log(w.getHeight());
	w.setHeight(h);

    });
}

function bridgeHandler(e)
{
    $A(all_files).each(function(f){
	processHandler(f.path);
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

	    // Only PDF Files
	    if (fid.fileName.match(/\.pdf$/))
	    {

		var r = $A(all_files).find(function(e){
		    return e.fileName == fid.fileName;
		});

		if (r)
		    return;

		all_files.push(fid);

		var elem = new Element("li");
		elem.innerHTML = fid.fileName;
		cont.appendChild(elem);
	    }
	}
    } catch(e){
	Titanium.API.log(e);
    }

}