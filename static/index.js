
document.addEventListener("DOMContentLoaded",function()
{
    const search = document.querySelector("input#search");
    search.addEventListener("input", searchFilter);
    function searchFilter(value)
    {
        const query = search.value;
        const links = document.querySelectorAll(".recipe-link");
        for (const link of links)
        {
            const text = link.querySelector(".recipe-title").textContent;
            const match = text.trim().toUpperCase().includes(query.toUpperCase());
            if (match)
            {
                link.classList.remove("hide");
            }
            else
            {
                link.classList.add("hide");
            }
        }
    }

});