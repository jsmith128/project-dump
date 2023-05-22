{/* <div class="vertical-menu">
    <a href="index.html">Main</a>
    <a href="schoolLinks.html">School</a>
    <a href="Page3.html">Page3</a>
    <br>
    <a href="rss.html" class="active">RSS</a>
    <br>
    <a href="https://www.google.com">Google</a>
</div> */}

// for creating the sidebar

var vert_menu = document.getElementsByClassName('vertical-menu')[0];
vert_menu.innerHTML =  `<a href="index.html" id="Main">New Tab</a>
                        <a href="schoolLinks.html" id="School">School</a>
                        <a href="Page3.html" id="Page3"></a>
                        <br>
                        <a href="tools.html" id="TOOLS">Tools</a>
                        <a href="rss.html" id="RSS">RSS</a>
                        <br>
                        <a href="https://www.google.com">Google</a>`;

title = document.title;
console.log(title);

if (title == "New Tab") {
    document.getElementById("Main").classList.add("active");
}

if (title == "School Links") {
    document.getElementById("School").classList.add("active");
}

if (title == "Page3") {
    document.getElementById("Page3").classList.add("active");
}

if (title == "Tool Links") {
    document.getElementById("TOOLS").classList.add("active");
}

if (title == "RSS Links") {
    document.getElementById("RSS").classList.add("active");
}