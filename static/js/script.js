

$(document).ready()
{
	var page = localStorage.getItem("page");

	if (page === null)
	{
		page = "home";
	}
	localStorage.setItem("page", page);
	$('#' + page).addClass('active').siblings().removeClass('active');
}

function changePage(page)
{
	var str_page = localStorage.getItem("page");

	if (str_page === page)
	{
		return;
	}
	localStorage.setItem("page", page);
	
	if (page === "home")
	{
		window.location.href = "/";
	}
	else
	{
		window.location.href = "/"+page;	
	}
	
}

function addTwitterLinks(url, display, text, index)
{
    'use strict';
    
    if (url === "" || url === null)
    {
        $('#tweet' + index).append("<p class='tweetDesc'>" +text+ "</p>");
    }
    else
    {
        var split = text.split(url),
            before = split[0],
            after = split[1];
        $('#tweet' + index).append("<p>" + before + "</p> <a class='tweetlink' target='_blank' style='color: #0000EE; float: left;' href='" +url+ "'>" +display + " </a><p> " + after + "</p>");    
    }
}
