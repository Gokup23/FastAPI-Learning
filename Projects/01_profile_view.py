from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/athlete/{name}", response_class=HTMLResponse)
async def athlete_bio(name: str):
     #Checking the path
    if "gopal" in name.lower() :
        html_content = """
        <html>
            <body style="font-family: Arial, sans-serif; background-color: #1a1a1a; color: white; text-align: center; padding: 50px;">
                <div style="border: 2px solid #00ffcc; padding: 30px; border-radius: 15px; display: inline-block; box-shadow: 0px 0px 20px #00ffcc;">
                    <h1 style="color: #00ffcc; text-transform: uppercase;">Athlete Profile: Gopal</h1>
                    <h3 style="color: #aaaaaa;">Goal: Dominant Aesthetic Silhouette</h3>
                    <hr style="border-color: #333;">
                    
                    <div style="text-align: left; font-size: 18px; line-height: 1.6;">
                        <p> <b>Height:</b> 6ft</p>
                        <p> <b>Weight:</b> 69 kg</p>
                        <p> <b>Body Fat:</b> 12%</p>
                        <p> <b>Shoulder Width:</b> 53.5 cm</p>
                        <p> <b>Waist:</b> 32 inches</p>
                        <p> <b>Neck:</b> 40 cm</p>
                    </div>
                </div>
            </body>
        </html>
        """
        return html_content
    
    #if a different name 
    else:
        return f"""
        <html>
            <body style="background-color: black; color: red; text-align: center; padding: 50px;">
                <h1>Error 404: Athlete '{name}' not found in database.</h1>
            </body>
        </html>
        """
