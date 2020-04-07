1. Briefly describe the differences between the webbrowser, requests, bs4, and selenium modules.
– webbrowser – Opens default browser to a specific page and that's about it. Documentation [here](https://docs.python.org/3.8/library/webbrowser.html). webbrowser comes installed with Python.
– requests – Module which allows you to download files and pages from the internet.
– bs4 – Beautiful Soup, version 4 is an HTML parser. This allows you to extract content from a web page.
– selenium – Module which launches and controls a web browser, allowing you to fill in forms and simulate mouse clicks.

2. What type of object is returned by requests.get()? How can you access the downloaded content as a string value?
It's a Response object: <class 'requests.models.Response'>. The object has a .text attribute which allows you to access the downloaded content as a string.

3. What requests method checks that the download worked?
The raise_for_status() method raises an exception if there's an error downloading the file. It will do nothing if the download succeeded.

4. How can you get the HTTP status code of a requests response?
A Response object has a status_code attribute. You can check it against requests.code.ok (i.e., Response.status_code == requests.codes.ok) to see if the status code was 200.

5. How do you save a requests response to a file?
You can use the open() function and write() method with a for loop. Example:
> import requests
> res = requests.get('https://automatetheboringstuff.com/files/rj.txt')
> res.raise_for_status()
> play_file = open('RomeoAndJuliet.txt', 'wb')
> for chunk in res.iter_content(100000):
>   play_file.write(chunk)
> play_file.close()

You have to open the file in write binary mode to maintain the Unicode encoding of the text.

6. What is the keyboard shortcut for opening a browser’s developer tools?
In Chrome on a Mac: Cmd + Option + I.

7. How can you view (in the developer tools) the HTML of a specific element on a web page?
Right-click or Control-click the element on the page, select Inspect Element. It'll bring up the Developer Tools window with the relevant HTML element selected.

8. What is the CSS selector string that would find the element with an id attribute of main?
'#main'

9. What is the CSS selector string that would find the elements with a CSS class of highlight?
'.highlight'

10. What is the CSS selector string that would find all the <div> elements inside another <div> element?
'div div'

11. What is the CSS selector string that would find the <button> element with a value attribute set to favorite?
'button[value="favorite"]'

12. Say you have a Beautiful Soup Tag object stored in the variable spam for the element <div>Hello, world!</div>. How could you get a string 'Hello, world!' from the Tag object?
spam.getText()

13. How would you store all the attributes of a Beautiful Soup Tag object in a variable named linkElem?
linkElem.attrs 

14. Running import selenium doesn’t work. How do you properly import the selenium module?
Run: from selenium import webdriver

15. What’s the difference between the find_element_* and find_elements_* methods?
– find_element_* – Returns a single WebElement object of the first element on the page matching your query.
– find_elements_* – Returns a list of WebElement_* objects for every matching element on the page.

16. What methods do Selenium’s WebElement objects have for simulating mouse clicks and keyboard keys?
– click() – Method for simulating mouse clicks.
– send_keys() – Method for simulating keyboard keys.

17. You could call send_keys(Keys.ENTER) on the Submit button’s WebElement object, but what is an easier way to submit a form with selenium?
Calling submit() on any element in a form will also submit the form. No need to specifically select the Submit button and call submit() on it.

18. How can you simulate clicking a browser’s Forward, Back, and Refresh buttons with selenium?
– browser.forward() – Clicks the Forward button.
– browser.back() – Clicks the Back button.
– browser.refresh() – Clicks the Refresh or Reload button.
– browser.quit() – Clicks the Close Window button.