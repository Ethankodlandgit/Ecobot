import discord
import os
from discord.ext  import commands
import random

intents = discord.Intents.default()
intents.messages = True
bot = commands.Bot(command_prefix='/', intents=intents)

dato_curioso=[
    "Un solo litro de aceite usado puede contaminar hasta 1 millón de litros de agua.",
    "El plástico tarda entre 100 y 1,000 años en descomponerse, dependiendo del tipo.",
    "Reciclar una lata de aluminio ahorra suficiente energía para encender una bombilla LED durante 20 horas.",
    "Las colillas de cigarro son la basura más común en playas y océanos.",
    "El transporte representa aproximadamente el 14 de las emisiones globales de gases de efecto invernadero.",
    "El vidrio es 100 reciclable y puede reutilizarse infinitamente sin perder calidad.",
    "El compostaje puede reducir la cantidad de basura que enviamos a los vertederos en un 30%.",
    "Las bolsas de tela reutilizables pueden reemplazar hasta 700 bolsas de plástico durante su vida útil.",
    "La contaminación del aire mata a 7 millones de personas cada año, según la OMS.",
    "Apagar las luces cuando no las necesitas puede reducir tus emisiones de carbono significativamente.",
    "Se estima que cada año se vierten al océano más de 8 millones de toneladas de plástico.",
    "Usar bicicletas o caminar en vez de conducir ayuda a reducir la contaminación del aire.",
    "Cada minuto se compra 1 millón de botellas de plástico en todo el mundo, pero menos del 10 se recicla.",
    "Plantar árboles puede absorber hasta 22 kg de dióxido de carbono por año, por árbol.",
    "Reparar en lugar de reemplazar aparatos electrónicos reduce la contaminación electrónica."
]

async def on_ready():
    print(f'¡Bot conectado como {bot.user}!')

@bot.command()
async def datocurioso(ctx):
    dato = random.choice(dato_curioso)
    await ctx.send(f'🌍 Dato curioso sobre la contaminación: {dato}')

preguntas_quiz = [
    {
        "pregunta": "¿Qué puedes hacer para reducir el uso de plástico?",
        "opciones": ["A) Usar bolsas reutilizables", "B) Comprar botellas de plástico", "C) No hacer nada"],
        "respuesta": "A"
    },
    {
        "pregunta": "¿Cuál es una fuente importante de contaminación del aire?",
        "opciones": ["A) Transporte público", "B) Fábricas", "C) Árboles"],
        "respuesta": "B"
    },
    {
        "pregunta": "¿Cuánto tarda en degradarse una bolsa de plástico?",
        "opciones": ["A) 10 años", "B) 100 años", "C) Hasta 500 años"],
        "respuesta": "C"
    },
    {
        "pregunta": "¿Cómo puedes ayudar a combatir la contaminación del agua?",
        "opciones": ["A) Tirar basura en ríos", "B) Evitar productos químicos", "C) Dejar el grifo abierto"],
        "respuesta": "B"
    },
        {
        "pregunta": "¿Qué es el compostaje?",
        "opciones": ["A) Crear fertilizante con desechos orgánicos", "B) Quemar basura", "C) Guardar comida sobrante"],
        "respuesta": "A"
    }
]

questions = [
    {
        "question": "¿Qué es la contaminación del aire?",
        "options": ["A) La presencia de sustancias nocivas en el aire", "B) Ruido excesivo", "C) Lluvia ácida"],
        "answer": "A"
    },
    {
        "question": "¿Cuál de estos es un gas contaminante?",
        "options": ["A) Oxígeno", "B) Nitrógeno", "C) Dióxido de carbono"],
        "answer": "C"
    },
    {
        "question": "¿Qué se debe hacer con el plástico para reducir la contaminación?",
        "options": ["A) Tirarlo en cualquier lugar", "B) Reciclarlo", "C) Quemarlo"],
        "answer": "B"
    }
]

recycling_tips = [
    "Lava los envases antes de reciclarlos para eliminar restos de comida.",
    "Separa los residuos según el tipo de material: plástico, vidrio, papel, etc.",
    "No mezcles materiales reciclables con basura común.",
    "Reutiliza los envases y bolsas siempre que sea posible.",
    "Infórmate sobre los puntos de reciclaje más cercanos a tu hogar.",
    "Usa contenedores de reciclaje adecuados y correctamente etiquetados."
]



@bot.command()
async def quiz(ctx):
    pregunta = random.choice(preguntas_quiz)
    opciones = "\n".join(pregunta["opciones"])
    mensaje = f"🌱 **{pregunta['pregunta']}**\n{opciones}\n\nResponde con A, B o C."
    
    await ctx.send(mensaje)

    def check(m):
        return m.author == ctx.author and m.content.upper() in ["A", "B", "C"]

    try:
        respuesta = await bot.wait_for('message', check=check, timeout=30.0)
        if respuesta.content.upper() == pregunta["respuesta"]:
            await ctx.send("✅ ¡Correcto! Cada pequeño esfuerzo cuenta para salvar el planeta. 🌍")
        else:
            await ctx.send(f"❌ Incorrecto. La respuesta correcta era {pregunta['respuesta']}. ¡Sigue aprendiendo!")
    except:
        await ctx.send("⏰ Tiempo agotado. ¡Inténtalo de nuevo!")
@bot.command()
async def aventura(ctx):
    await ctx.send("🌱 **Bienvenido a EcoAventura** 🌍\nTu misión es salvar el planeta. Elige tu rol para comenzar la aventura:\n\n1️⃣ Eco-guerrero\n2️⃣ Guardabosques\n\nResponde con `1` o `2`.")

    def check(m):
        return m.author == ctx.author and m.content in ["1", "2"]

    try:
        rol = await bot.wait_for('message', check=check, timeout=30.0)
        personaje = "Eco-guerrero" if rol.content == "1" else "Guardabosques"
        
        await ctx.send(f"🔋 ¡Has elegido ser un {personaje}! Comienza tu misión para salvar el medio ambiente. 🌳")
        puntos = 0  


        await ctx.send("🎮 ¡Estás a punto de comenzar tu misión!\nTus decisiones afectarán el futuro de nuestro planeta. ¿Estás listo?")

        # Misión 1
        await ctx.send("🚮 **Misión 1:** Estás en la playa y ves basura por todos lados. ¿Qué haces?\n\nA) Recoger toda la basura y clasificarla.\nB) Ignorarla y seguir disfrutando de la vista.\n\nResponde con `A` o `B`.")

        def check_decision(m):
            return m.author == ctx.author and m.content.upper() in ["A", "B"]

        decision1 = await bot.wait_for('message', check=check_decision, timeout=30.0)

        if decision1.content.upper() == "A":
            await ctx.send("✅ ¡Gran trabajo! Has ayudado a limpiar la playa y proteger la fauna marina. +15 puntos. 🐚")
            puntos += 15
        else:
            await ctx.send("❌ Ignorar la basura contamina el océano. -5 puntos. 🌊")
            puntos -= 5

        # Misión 2
        await ctx.send("💧 **Misión 2:** En tu hogar, dejas la ducha abierta mientras te cepillas los dientes. ¿Qué haces?\n\nA) Cerrar la ducha mientras me cepillo los dientes.\nB) Dejar la ducha abierta porque no importa.\n\nResponde con `A` o `B`.")

        decision2 = await bot.wait_for('message', check=check_decision, timeout=30.0)

        if decision2.content.upper() == "A":
            await ctx.send("✅ ¡Perfecto! Estás ahorrando agua y cuidando un recurso vital. +10 puntos. 💧")
            puntos += 10
        else:
            await ctx.send("❌ Dejar la ducha abierta desperdicia agua. -5 puntos. 🚿")
            puntos -= 5

        # Misión 3
        await ctx.send("🌫️ **Misión 3:** Estás viajando en auto y ves una bicicleta. ¿Qué decides?\n\nA) Usar la bicicleta para reducir las emisiones de CO2.\nB) Continuar usando el automóvil por comodidad.\n\nResponde con `A` o `B`.")

        decision3 = await bot.wait_for('message', check=check_decision, timeout=30.0)

        if decision3.content.upper() == "A":
            await ctx.send("✅ ¡Excelente! Usar la bicicleta ayuda a reducir las emisiones de CO2. +20 puntos. 🚲")
            puntos += 20
        else:
            await ctx.send("❌ Usar el automóvil contribuye a la contaminación. -10 puntos. 🚗")
            puntos -= 10

        # Misión 4
        await ctx.send("🌳 **Misión 4:** Caminas por un bosque y ves una gran área de tierra talada. ¿Qué haces?\n\nA) Organizar una protesta para detener la deforestación.\nB) Ignorar el problema porque no es tu responsabilidad.\n\nResponde con `A` o `B`.")

        decision4 = await bot.wait_for('message', check=check_decision, timeout=30.0)

        if decision4.content.upper() == "A":
            await ctx.send("✅ ¡Has hecho una gran diferencia! Has dado visibilidad al problema. +25 puntos. 🌳")
            puntos += 25
        else:
            await ctx.send("❌ Ignorar la deforestación pone en peligro nuestros ecosistemas. -15 puntos. 🌍")
            puntos -= 15

        # Misión 5
        await ctx.send("♻️ **Misión 5:** Estás en la ciudad y ves un contenedor de reciclaje lleno de basura mezclada. ¿Qué haces?\n\nA) Reciclar adecuadamente y educar a los demás.\nB) Tirar tu basura en el contenedor sin preocuparte por clasificarla.\n\nResponde con `A` o `B`.")

        decision5 = await bot.wait_for('message', check=check_decision, timeout=30.0)

        if decision5.content.upper() == "A":
            await ctx.send("✅ ¡Excelente elección! El reciclaje correcto ayuda a reducir la contaminación. +20 puntos. ♻️")
            puntos += 20
        else:
            await ctx.send("❌ Tirar basura incorrectamente empeora el problema. -10 puntos.")
            puntos -= 10

        # Misión 6
        await ctx.send("🥕 **Misión 6:** Estás en un supermercado y ves carne, pero sabes que su producción tiene un gran impacto ambiental. ¿Qué decides?\n\nA) Comprar alimentos vegetales y sostenibles.\nB) Comprar carne porque es lo que prefieres.\n\nResponde con `A` o `B`.")

        decision6 = await bot.wait_for('message', check=check_decision, timeout=30.0)

        if decision6.content.upper() == "A":
            await ctx.send("✅ ¡Excelente elección! Reducir el consumo de carne ayuda a combatir el cambio climático. +30 puntos. 🌱")
            puntos += 30
        else:
            await ctx.send("❌ Consumir carne de manera insostenible contribuye a la contaminación. -20 puntos. 🍖")
            puntos -= 20

        # Misión 7
        await ctx.send("⚡ **Misión 7:** Vives en una casa que usa electricidad de fuentes no renovables. ¿Qué haces?\n\nA) Instalar paneles solares para generar energía limpia.\nB) Dejar las cosas como están, ya que no parece un gran problema.\n\nResponde con `A` o `B`.")

        decision7 = await bot.wait_for('message', check=check_decision, timeout=30.0)

        if decision7.content.upper() == "A":
            await ctx.send("✅ ¡Has tomado una gran decisión! Usar energía renovable reduce las emisiones de carbono. +35 puntos. 🌞")
            puntos += 35
        else:
            await ctx.send("❌ No hacer nada para reducir el impacto ambiental empeora el problema. -20 puntos.")
            puntos -= 20

        await ctx.send(f"🎉 **Fin de la aventura:** Has completado tu misión con {puntos} puntos.\n")
        
        if puntos > 100:
            await ctx.send("🌟 ¡Eres un verdadero héroe ecológico! ¡El planeta te agradece tus esfuerzos! 🌍")
        elif puntos > 50:
            await ctx.send("🌱 ¡Lo hiciste bien! Pero aún hay mucho que podemos hacer. Sigue luchando por nuestro planeta. 🌏")
        else:
            await ctx.send("⚠️ ¡Tu puntaje indica que hay mucho por mejorar! Cada pequeña acción cuenta, ¡sigue aprendiendo y mejorando! 🌍")

    except:
        await ctx.send("⏰ No respondiste a tiempo. ¡Inténtalo de nuevo!")
@bot.command()
async def adivina(ctx):
    palabras_ecologicas = {
        "reciclaje": "Es el proceso de convertir materiales usados en nuevos productos.",
        "biodiversidad": "Se refiere a la variedad de organismos vivos en un ecosistema.",
        "sostenibilidad": "Es la capacidad de mantener un equilibrio ecológico sin agotar los recursos.",
        "contaminacion": "Es la presencia de sustancias nocivas en el aire, agua o suelo.",
        "desechos": "Son los restos o productos que ya no tienen utilidad y deben ser eliminados.",
        "reforestacion": "Es el proceso de plantar árboles para restaurar áreas deforestadas.",
        "energia": "Es la capacidad de realizar trabajo, como la que se obtiene de fuentes renovables.",
        "ecosistema": "Es un conjunto de seres vivos que interactúan con su entorno físico.",
        "agua": "Es el líquido vital para la vida en la Tierra, indispensable para las plantas, animales y seres humanos.",
        "calentamiento global": "Es el aumento de la temperatura de la atmósfera terrestre, relacionado con la actividad humana."
    }

    palabra, pista = random.choice(list(palabras_ecologicas.items()))
    
    await ctx.send(f"💡 **Pista**: {pista}\nAdivina la palabra relacionada con el medio ambiente. Responde con la palabra correcta.")
    
    def check(m):
        return m.author == ctx.author and m.content.lower() == palabra.lower()

    try:
        respuesta = await bot.wait_for('message', check=check, timeout=30.0)
        await ctx.send(f"✅ ¡Correcto! La palabra es **{palabra}**. ¡Bien hecho! 🌱")
    except:
        await ctx.send(f"❌ ¡Tiempo agotado! La respuesta correcta era **{palabra}**. ¡Inténtalo la próxima vez! 🌍")

async def help(ctx):
    comandos = """
    **🌍 Comandos disponibles:**
    
    1. **/datocurioso**: 🌱 Obtén un dato curioso sobre la contaminación y cómo combatirla.
    2. **/quiz**: 🧠 Participa en un quiz ecológico con preguntas de opción múltiple.
    3. **/adivina**: 🤔 Adivina la palabra ecológica basándote en una pista.
    4. **/juegobasura**: 🗑️ Juega clasificando basura en el contenedor correcto. ¡Demuestra tus habilidades de reciclaje!
    """
    await ctx.send(comandos)



bot.run('MTMxMjQ5NDAzMjI4NjY0NjM3Mw.Gfc5H7.mz2iDgixCEhCDYXfopvPlrijRQOHol6cLZp1Jo')