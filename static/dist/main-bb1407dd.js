const u=document.querySelector("#toggle-nav-sidebar"),i=document.querySelector("#navbar-menu"),c=i.querySelector("button"),g=document.querySelectorAll(".desktop-nav-menu"),p=document.querySelector("#toggle-search-form"),n=document.querySelector("#search-container"),f=n.querySelector('button[type="reset"]'),b=document.createElement("div"),s=(e,t,l,v)=>{l&&e.setAttribute("aria-expanded",l),t.setAttribute("aria-hidden",v)},a=(e,t,l)=>{e.classList[l](t)};u.addEventListener("click",()=>{a(i,"open","toggle"),s(u,i,"true","false"),s(c,i,"true","false"),window.addEventListener("resize",()=>{window.innerWidth>1024&&(i.classList.remove("open"),i.setAttribute("aria-hidden","true"),c.setAttribute("aria-expanded","false"))})});c.addEventListener("click",()=>{a(i,"open","toggle"),s(u,i,"false","true"),s(c,i,"false","true")});g.forEach(e=>{e.addEventListener("mouseover",()=>{s(e,e.nextElementSibling,!1,"false"),a(e.nextElementSibling,"open","add")}),e.addEventListener("mouseleave",()=>{s(e,e.nextElementSibling,!1,"true"),a(e.nextElementSibling,"open","remove")}),e.nextElementSibling.addEventListener("mouseenter",()=>{s(e,e.nextElementSibling,!1,"false"),a(e.nextElementSibling,"open","add")}),e.nextElementSibling.addEventListener("mouseleave",()=>{s(e,e.nextElementSibling,!1,"true"),a(e.nextElementSibling,"open","remove")})});p.addEventListener("click",()=>{n.classList.toggle("open"),n.querySelector("input").focus(),document.body.appendChild(b),d(),window.addEventListener("scroll",S),E()});function d(){const e=n.classList.contains("open");g.forEach(t=>{t.setAttribute("aria-hidden",e?"true":"false"),e?t.setAttribute("inert","true"):t.removeAttribute("inert")}),b.classList.toggle("overlay",e)}function E(){document.body.addEventListener("click",e=>{e.target===b&&(n.classList.toggle("open"),n.setAttribute("aria-hidden","true"),d())}),document.addEventListener("keydown",e=>{e.key==="Escape"&&n.classList.contains("open")&&(n.classList.toggle("open"),n.setAttribute("aria-hidden","true"),d())})}function S(){window.scrollY>150&&(n.classList.remove("open"),n.setAttribute("aria-hidden","true"),d())}f.addEventListener("click",()=>{n.classList.toggle("open"),n.setAttribute("aria-hidden","true"),d()});const r=document.querySelector("#cart-navigation"),o=document.querySelector("#cart-popover");function h(){o.setAttribute("aria-hidden","false")}function m(){o.getAttribute("aria-hidden")==="true"&&r.getAttribute("aria-expanded")==="true"&&(r.setAttribute("aria-expanded","false"),o.setAttribute("aria-hidden","true"))}r==null||r.addEventListener("mouseover",h);r==null||r.addEventListener("mouseleave",m);o==null||o.addEventListener("mouseleave",()=>o.setAttribute("aria-hidden","true"));setTimeout(()=>{const e=document.querySelectorAll("[data-django-message]");e&&e.forEach(t=>{t.style.transition="opacity 0.5s",t.style.opacity="0",setTimeout(()=>{t.parentNode.removeChild(t)},500)})},4e3);
