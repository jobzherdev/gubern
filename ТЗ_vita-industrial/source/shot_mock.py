import asyncio, json
from playwright.async_api import async_playwright
BASE="file:///tmp/claude-0/-home-user-gubern/89e05905-ac31-57ad-961e-363c08a6c223/scratchpad/build/"
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch(executable_path="/opt/pw-browsers/chromium-1194/chrome-linux/chrome",
                                  args=["--no-sandbox","--font-render-hinting=none"])
        ctx=await b.new_context(viewport={"width":1440,"height":1000},device_scale_factor=1.5)
        pg=await ctx.new_page()
        await pg.goto(BASE+"mock.html")
        await pg.evaluate("document.fonts.ready")
        await pg.wait_for_timeout(4000)
        # замер и скриншот — в одном состоянии страницы
        data=await pg.evaluate("""() => ({
            h: document.body.scrollHeight,
            secs: Array.from(document.querySelectorAll('section')).map(s=>({
                top: s.getBoundingClientRect().top + window.scrollY,
                h: s.getBoundingClientRect().height,
                label: (s.querySelector('.lbl')||{}).textContent||''}))})""")
        await pg.screenshot(path="shots/mock_full.png", full_page=True)
        json.dump(data["secs"], open('sections.json','w'), ensure_ascii=False, indent=1)
        print("page height", data["h"], "sections", len(data["secs"]),
              "last bottom", round(data["secs"][-1]["top"]+data["secs"][-1]["h"]))
        await ctx.close()
        ctx2=await b.new_context(viewport={"width":390,"height":844},device_scale_factor=3,is_mobile=True)
        pg2=await ctx2.new_page()
        await pg2.goto(BASE+"mock_mobile.html")
        await pg2.evaluate("document.fonts.ready")
        await pg2.wait_for_timeout(3000)
        await pg2.screenshot(path="shots/mock_mobile.png")
        await ctx2.close(); await b.close()
asyncio.run(main())
