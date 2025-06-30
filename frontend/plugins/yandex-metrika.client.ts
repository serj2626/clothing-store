// export default defineNuxtPlugin((nuxtApp) => {
//   const METRIKA_ID = 12345678; // ЗАМЕНИ НА СВОЙ ID

//   // Добавить скрипт Метрики
//   const script = document.createElement("script");
//   script.innerHTML = `
//     (function(m,e,t,r,i,k,a){
//       m[i]=m[i]||function(){(m[i].a=m[i].a||[]).push(arguments)}
//       m[i].l=1*new Date()
//       k=e.createElement(t),a=e.getElementsByTagName(t)[0]
//       k.async=1;k.src=r;a.parentNode.insertBefore(k,a)
//     })(window, document, "script", "https://mc.yandex.ru/metrika/tag.js", "ym");

//     ym(${METRIKA_ID}, "init", {
//         clickmap:true,
//         trackLinks:true,
//         accurateTrackBounce:true,
//         webvisor:true
//     });
//   `;
//   document.head.appendChild(script);

//   // <noscript> для SEO
//   const noScript = document.createElement("noscript");
//   noScript.innerHTML = `
//     <div><img src="https://mc.yandex.ru/watch/${METRIKA_ID}" style="position:absolute; left:-9999px;" alt="" /></div>
//   `;
//   document.body.appendChild(noScript);

//   // Отслеживание переходов (SPA-режим)
//   nuxtApp.hook("page:finish", () => {
//     if (typeof window.ym === "function") {
//       window.ym(METRIKA_ID, "hit", window.location.href);
//     }
//   });
// });
