const elementToPlainText = (element) => {
    let text = element?.textContent || '';
    text = text.trim().replace(/\s+/g, ' '); // Remove extra whitespace
    return text;
}

const removeHtmlTags = (html) => {
    const div = document.createElement('div');
    div.innerHTML = html;
    return div.innerText || div.textContent || '';
}

const parseDescription = () => {
    let url = window.location.href
    let element;
    if (url.includes("indeed")) {
        element = document.getElementById("jobDescriptionText")
    }
    else if (url.includes("linked")) {
        element = document.getElementById("job-details")
        element = element?.getElementsByClassName("mt4").item(0)
    }

    // Select elements with class names containing the keyword
    // const elements = document.querySelectorAll(`[class*="j${keyword}"]`);
    return removeHtmlTags(elementToPlainText(element));
}
const parseCompany = () => {
    let url = window.location.href
    let element;
    if (url.includes("indeed")) {//indeed.com
        element = document.querySelectorAll('[data-company-name]')?.item(0).getElementsByTagName('a')?.item(0);
    }
    else if (url.includes("linked")) {//Linked in
        element = document.getElementsByClassName("job-details-jobs-unified-top-card__primary-description-without-tagline mb2").item(0)?.getElementsByTagName('a')?.item(0)
    }

    // Select elements with class names containing the keyword
    // const elements = document.querySelectorAll(`[class*="j${keyword}"]`);
    // console.log();
    return removeHtmlTags(elementToPlainText(element))
}


chrome.runtime.onMessage.addListener(
    function (request, sender, sendResponse) {
        console.log(sender.tab ?
            "from a content script:" + sender.tab.url :
            "from the extension");

        if (request.type === "scan") {
            var scanResults={
                company:parseCompany(),
                description:parseDescription()
                
            };
            console.log(scanResults);
            sendResponse(scanResults);
        }
        return 1;
    }
);

console.log("RAN");