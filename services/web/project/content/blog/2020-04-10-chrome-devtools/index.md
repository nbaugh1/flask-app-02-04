---
title: "Chrome Dev Tools"
date: 2020-04-10
published: true
---

I decided to spend the day today learning about how to use Chrome DevTools. Using browser developer consoles is an integral part of developing web applications and they offer a wide range of tools that can make life a lot easier than sticking within your IDE. While `console.log()` might always be the quickest goto debugging tool for JavaScript, I felt needed to add more to my skillset. Aside from `console.log()`, I make heavy use of `debugger` to set breakpoints within my code. This allows me to drop into the developer's console and test out code or inspect variables within a specific scope. There are times, though, when it isn't possible to use `debugger` in a specific part of your code. The use of Breakpoints provided by the Dev Tools allows me to stop and inspect code at certian points simillarly to `debugger`.

Breakpoints are found in the Sources tab in Chrome DevTools and can be used in a variey of ways. First up is **Event Listener Breakpoints**. An event listener breakpoint pauses the execution your code and highlights the function called at the occruance your chosen event (such as mouse clicks, drag and drop, clipboard actions etc...). You can then use the controls to step through your code line by line or step over to the nect function call.   

Next is a **Line-of-Code Breakpoint**. A line-of-code break point can be set at a specific line of code (duh) by opening your javascript file from the file browser section, then clicking the number to the left of the line of code that you want to stop at. From here DevTools provides lots of ways to inspect the value of your variables. The thrid pane within your Sources tab is the Scope pane. Here DevTools provides dropdowns listing the values of both local and golbal vaiables. You can also set Watch Expressions which will update based on the expression provided, such as the `typeOf` a variable (ie `String` or `Integer`)

Changes can be tested within the DevTools console and then applied into the code editor inside of your Sources tab. 
All of this, as well as an interactive tutorial are found on the Chrome DevTools Doc site. https://developers.google.com/web/tools/chrome-devtools/javascript

