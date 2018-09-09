// Initialize Firebase
var config = {
	apiKey: "AIzaSyCKQl74vgI56uxAGqVWYwAO_YmR6XoFwGo",
    authDomain: "images-5a37d.firebaseapp.com",
    databaseURL: "https://images-5a37d.firebaseio.com",
    projectId: "images-5a37d",
    storageBucket: "images-5a37d.appspot.com",
    messagingSenderId: "740161466118"
};
firebase.initializeApp(config);

var db = firebase.database();
var img1 = document.getElementById('image1');
var names = db.ref('image_refrences');

//Create a 3d array to fill our data with
var name_data = [];


function search_image_from_database(){
	//Extract data from the database
	var tag;
	names.on('value', function(snapshot) {
		snapshot.forEach(function(childSnapshot) {
			var childData = childSnapshot.val();

			var name = childData.name;
			var reason = childData.reason;

			name_data.push([name, reason]);
			extract_done = true;
			//console.log(tag)
		});
	});
}

search_image_from_database();

window.setTimeout(function(){
	var pg = $("#rayers");
	for(var i = 0; i < name_data.length; i++){
		k = "<li> <p class = \"name\">" + name_data[i][0] + "</p> <p class = \"reason\">" + name_data[i][1] + "</p> </li>"
		pg.append(k);
	}
}, 1000)