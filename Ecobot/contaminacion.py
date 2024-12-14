import discord
import os
from discord.ext  import commands
import random
from model import get_class 
import requests 

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

        # Misión 8
        await ctx.send("🌾 **Misión 8:** Tienes la oportunidad de plantar un árbol en tu comunidad. ¿Qué haces?\n\nA) Plantar un árbol y comprometerme a cuidar de él.\nB) Decidir que un árbol no hace gran diferencia.\n\nResponde con `A` o `B`.")

        decision8 = await bot.wait_for('message', check=check_decision, timeout=30.0)

        if decision8.content.upper() == "A":
            await ctx.send("✅ ¡Excelente! Plantar árboles ayuda a reducir el CO2 y promueve la biodiversidad. +40 puntos. 🌱")
            puntos += 40
        else:
            await ctx.send("❌ No plantar un árbol deja de lado una de las mejores maneras de combatir el cambio climático. -15 puntos.")
            puntos -= 15

        # Misión 9
        await ctx.send("🌿 **Misión 9:** Estás en el campo y puedes elegir entre usar pesticidas químicos o buscar alternativas orgánicas. ¿Qué haces?\n\nA) Usar pesticidas orgánicos.\nB) Usar pesticidas químicos para hacerlo rápido.\n\nResponde con `A` o `B`.")

        decision9 = await bot.wait_for('message', check=check_decision, timeout=30.0)

        if decision9.content.upper() == "A":
            await ctx.send("✅ ¡Genial! Los pesticidas orgánicos ayudan a preservar la salud del suelo y los ecosistemas. +25 puntos. 🌻")
            puntos += 25
        else:
            await ctx.send("❌ Los pesticidas químicos dañan el suelo y la biodiversidad. -10 puntos. 🐝")
            puntos -= 10

        # Misión 10
        await ctx.send("🚶 **Misión 10:** En tu comunidad hay muchos automóviles, y el aire está contaminado. ¿Qué haces?\n\nA) Promover el uso de transporte público o vehículos eléctricos.\nB) Continuar usando tu automóvil como siempre.\n\nResponde con `A` o `B`.")

        decision10 = await bot.wait_for('message', check=check_decision, timeout=30.0)

        if decision10.content.upper() == "A":
            await ctx.send("✅ ¡Gran iniciativa! Reducir el uso del automóvil ayuda a combatir la contaminación del aire. +30 puntos. 🚎")
            puntos += 30
        else:
            await ctx.send("❌ No reducir el uso del automóvil aumenta la contaminación. -15 puntos.")
            puntos -= 15

        # Resumen final
        await ctx.send(f"🎉 **Fin de la aventura:** Has completado tu misión con {puntos} puntos.\n")
        
        if puntos > 200:
            await ctx.send("🌟 ¡Eres un verdadero héroe ecológico! ¡El planeta te agradece tus esfuerzos! 🌍")
        elif puntos > 100:
            await ctx.send("🌱 ¡Lo hiciste bien! Pero aún hay mucho que podemos hacer. Sigue luchando por nuestro planeta. 🌏")
        else:
            await ctx.send("⚠️ ¡Tu puntaje indica que hay mucho por mejorar! Cada pequeña acción cuenta, ¡sigue aprendiendo y mejorando! 🌍")

    except:
        await ctx.send("⏰ No respondiste a tiempo. ¡Inténtalo de nuevo!")

@bot.command()
async def adivinanza_ecologica(ctx):
    # Lista de adivinanzas ecológicas
    adivinanzas = [
        {
            "pregunta": "Soy invisible, pero puedo dañar el planeta. Provoco el calentamiento global. ¿Qué soy?",
            "respuesta": "dióxido de carbono (CO2)",
            "puntos": 20
        },
        {
            "pregunta": "¿Qué animal es crucial para la polinización y está en peligro de extinción por la pérdida de hábitats?",
            "respuesta": "abeja",
            "puntos": 25
        },
        {
            "pregunta": "Soy el recurso natural más usado, pero estoy en peligro por el cambio climático. ¿Qué soy?",
            "respuesta": "agua",
            "puntos": 15
        },
        {
            "pregunta": "Aunque me cortas y me haces pedazos, sigo siendo importante para el ecosistema. ¿Qué soy?",
            "respuesta": "árbol",
            "puntos": 30
        },
        {
            "pregunta": "Me encuentras en el mar, soy una fuente de energía renovable. ¿Qué soy?",
            "respuesta": "olas",
            "puntos": 20
        },
        {
            "pregunta": "Soy una capa en la atmósfera que nos protege de los rayos del sol. Si me dañas, pueden aumentar los casos de cáncer de piel. ¿Qué soy?",
            "respuesta": "capa de ozono",
            "puntos": 40
        },
        {
            "pregunta": "Estoy hecho de material biodegradable y puedes usarme para reducir los residuos plásticos. ¿Qué soy?",
            "respuesta": "pañales biodegradables",
            "puntos": 35
        },
        {
            "pregunta": "Soy el cambio en los patrones climáticos causados principalmente por las actividades humanas. ¿Qué soy?",
            "respuesta": "cambio climático",
            "puntos": 50
        },
        {
            "pregunta": "Puedo ser reutilizado para fabricar nuevos productos. Cuando no me reciclas, me convierto en basura. ¿Qué soy?",
            "respuesta": "plástico",
            "puntos": 15
        },
        {
            "pregunta": "Soy una fuente de energía renovable que depende de la radiación solar. ¿Qué soy?",
            "respuesta": "energía solar",
            "puntos": 25
        }
    ]
    
    # Introducción a la actividad
    await ctx.send("🌱 **Adivinanza Ecológica Extensa** 🌍\n\n¡Vamos a poner a prueba tus conocimientos sobre el medio ambiente! Responde las adivinanzas para ganar puntos. ¡Prepárate para aprender y divertirte! 🎉\n")
    
    total_puntos = 0
    
    for i in range(3):  # Realizamos 3 rondas de adivinanzas
        # Selección aleatoria de una adivinanza
        import random
        adivinanza = random.choice(adivinanzas)
        
        # Enviar la pregunta
        await ctx.send(f"🔍 **Adivinanza {i+1}:**\n{adivinanza['pregunta']}\n\nResponde con tu respuesta.")
        
        def check(m):
            return m.author == ctx.author
        
        try:
            # Esperar la respuesta del usuario
            respuesta = await bot.wait_for('message', check=check, timeout=30.0)
            
            # Verificar la respuesta
            if respuesta.content.lower() == adivinanza['respuesta'].lower():
                await ctx.send(f"✅ ¡Correcto! La respuesta es {adivinanza['respuesta']}. +{adivinanza['puntos']} puntos.")
                total_puntos += adivinanza['puntos']
            else:
                await ctx.send(f"❌ ¡Incorrecto! La respuesta correcta era: {adivinanza['respuesta']}. No ganaste puntos en esta ronda.")
            
        except:
            await ctx.send("⏰ ¡Tiempo agotado! No respondiste a tiempo. Intenta de nuevo cuando estés listo.")
    
    # Resumen final de puntos
    if total_puntos >= 100:
        await ctx.send(f"🌟 ¡Impresionante! Has acumulado {total_puntos} puntos. Eres un experto ecológico. ¡Sigue aprendiendo y cuidando el planeta! 🌍")
    elif total_puntos >= 50:
        await ctx.send(f"🌱 ¡Bien hecho! Has acumulado {total_puntos} puntos. ¡Sigue protegiendo el medio ambiente! 🌏")
    else:
        await ctx.send(f"⚠️ ¡Aún tienes mucho por aprender! Has acumulado {total_puntos} puntos. ¡No te rindas, sigue sumando conocimiento y acción por el planeta! 🌍")

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
@bot.command()
async def sabio_ecologico(ctx):
    # Introducción
    await ctx.send("🌿 **El Sabio Ecológico** 🌍\n\nBienvenido, joven aprendiz. El Sabio Ecológico te ha llamado para que demuestres tus conocimientos sobre el mundo natural. Responde las preguntas correctamente y obtén la sabiduría ecológica. ¡Buena suerte! 🍃")

    # Lista de preguntas y respuestas
    preguntas = [
        {
            "pregunta": "¿Cuál es la principal causa del cambio climático?",
            "respuestas": ["La deforestación", "El uso de combustibles fósiles", "El reciclaje", "La energía solar"],
            "respuesta_correcta": "El uso de combustibles fósiles",
            "puntos": 30
        },
        {
            "pregunta": "¿Qué recurso natural renovable podemos utilizar para generar electricidad sin dañar el medio ambiente?",
            "respuestas": ["Gas natural", "Energía solar", "Carbón", "Energía nuclear"],
            "respuesta_correcta": "Energía solar",
            "puntos": 25
        },
        {
            "pregunta": "¿Qué animal es conocido por ser un excelente indicador de la salud de un ecosistema?",
            "respuestas": ["León", "Rana", "Elefante", "Lobo"],
            "respuesta_correcta": "Rana",
            "puntos": 20
        },
        {
            "pregunta": "¿Qué es la biodiversidad?",
            "respuestas": [
                "La variedad de especies de seres vivos en un ecosistema.",
                "La cantidad de agua disponible en el planeta.",
                "La cantidad de carbono en la atmósfera.",
                "El número de bosques en el mundo."
            ],
            "respuesta_correcta": "La variedad de especies de seres vivos en un ecosistema.",
            "puntos": 25
        },
        {
            "pregunta": "¿Qué actividad humana contribuye más a la contaminación del agua?",
            "respuestas": ["El reciclaje", "El vertido de productos químicos", "La plantación de árboles", "El uso de energía renovable"],
            "respuesta_correcta": "El vertido de productos químicos",
            "puntos": 30
        },
        {
            "pregunta": "¿Cuál es el impacto principal de la deforestación?",
            "respuestas": ["Aumenta la biodiversidad", "Disminuye el nivel de oxígeno en el aire", "Destruye los hábitats naturales", "Aumenta la cantidad de agua disponible"],
            "respuesta_correcta": "Destruye los hábitats naturales",
            "puntos": 40
        },
    ]

    total_puntos = 0
    # Preguntar por las respuestas
    for i, pregunta in enumerate(preguntas, start=1):
        await ctx.send(f"🧠 **Pregunta {i}:** {pregunta['pregunta']}")
        await ctx.send("\n".join([f"{idx + 1}) {respuesta}" for idx, respuesta in enumerate(pregunta["respuestas"])]))
        
        def check(m):
            return m.author == ctx.author and m.content in ["1", "2", "3", "4"]
        
        try:
            respuesta_usuario = await bot.wait_for('message', check=check, timeout=30.0)
            respuesta_usuario = int(respuesta_usuario.content)
            
            # Verificar la respuesta
            if pregunta["respuestas"][respuesta_usuario - 1] == pregunta["respuesta_correcta"]:
                await ctx.send(f"✅ ¡Correcto! La respuesta es {pregunta['respuesta_correcta']}. +{pregunta['puntos']} puntos.")
                total_puntos += pregunta["puntos"]
            else:
                await ctx.send(f"❌ ¡Incorrecto! La respuesta correcta era: {pregunta['respuesta_correcta']}. No ganaste puntos en esta ronda.")
        
        except:
            await ctx.send("⏰ ¡Tiempo agotado! No respondiste a tiempo. ¡Intentemos de nuevo en la siguiente pregunta!")

    # Resumen final de puntos
    if total_puntos >= 150:
        await ctx.send(f"🌟 ¡Sabio Ecológico en formación! Has acumulado {total_puntos} puntos. Estás listo para proteger nuestro planeta con tu sabiduría. 🌍")
    elif total_puntos >= 100:
        await ctx.send(f"🌱 ¡Buen trabajo! Has acumulado {total_puntos} puntos. Sigue aprendiendo y aplicando tus conocimientos ecológicos. 🌏")
    else:
        await ctx.send(f"⚠️ ¡Aún tienes mucho que aprender! Has acumulado {total_puntos} puntos. La sabiduría ecológica llega con el tiempo, sigue creciendo. 🌍")
@bot.command()
async def diario_ecologico(ctx):
    # Introducción
    await ctx.send("🌿 **El Diario Ecológico** 🌍\n\nBienvenido al Diario Ecológico. Cada día que tomes una acción positiva para el medio ambiente, ganarás puntos. ¡Empieza a registrar tus acciones y conviértete en un verdadero protector del planeta! 🌱")

    # Definir las acciones posibles y sus puntos
    acciones = {
        "reciclaje": {
            "descripcion": "Reciclaste materiales como papel, plástico o vidrio.",
            "puntos": 20
        },
        "ahorro_agua": {
            "descripcion": "Redujiste el consumo de agua (cerraste el grifo mientras te cepillabas los dientes, etc.).",
            "puntos": 15
        },
        "uso_transporte_publico": {
            "descripcion": "Usaste transporte público o bicicleta en lugar de coche.",
            "puntos": 25
        },
        "reforestacion": {
            "descripcion": "Participaste en una actividad de reforestación o plantaste un árbol.",
            "puntos": 30
        },
        "reduccion_residuos": {
            "descripcion": "Disminuiste la cantidad de residuos que generas (usaste productos reutilizables, evitaste el plástico de un solo uso, etc.).",
            "puntos": 20
        },
        "energia_renovable": {
            "descripcion": "Usaste energía renovable o ahorraste energía eléctrica.",
            "puntos": 25
        }
    }

    # Introducir el ciclo de registro
    total_puntos = 0
    continuar = True

    while continuar:
        # Solicitar al usuario que registre una acción ecológica
        await ctx.send("📝 **Registra una acción ecológica que hayas hecho hoy para ganar puntos.**\n\nElige una acción de las siguientes opciones:\n"
                       "1️⃣ Reciclaje\n2️⃣ Ahorro de agua\n3️⃣ Uso de transporte público o bicicleta\n4️⃣ Reforestación\n5️⃣ Reducción de residuos\n6️⃣ Uso de energía renovable\n\nEscribe el número de la acción que realizaste o escribe `fin` para terminar.")

        def check(m):
            return m.author == ctx.author and (m.content in ["1", "2", "3", "4", "5", "6", "fin"])

        try:
            # Esperar la respuesta del usuario
            respuesta = await bot.wait_for('message', check=check, timeout=60.0)

            if respuesta.content == "fin":
                continuar = False
                break

            accion_seleccionada = list(acciones.values())[int(respuesta.content) - 1]
            await ctx.send(f"✅ ¡Excelente! Hoy realizaste la acción: **{accion_seleccionada['descripcion']}**. +{accion_seleccionada['puntos']} puntos.")
            total_puntos += accion_seleccionada["puntos"]

        except:
            await ctx.send("⏰ ¡Tiempo agotado! Intenta nuevamente.")

    # Mostrar el puntaje final
    await ctx.send(f"🎉 **Fin del Diario Ecológico:** Hoy acumulaste {total_puntos} puntos por tus acciones ecológicas. ¡Gracias por cuidar el planeta! 🌍")

    if total_puntos >= 100:
        await ctx.send("🌟 ¡Fantástico! Has sido un verdadero héroe ecológico hoy. Sigue así para proteger nuestro planeta.")
    elif total_puntos >= 50:
        await ctx.send("🌱 ¡Bien hecho! Has hecho un buen trabajo, pero aún hay más por hacer. ¡Sigue luchando por la Tierra!")
    else:
        await ctx.send("⚠️ ¡Puedes hacerlo mejor! Cada acción cuenta, sigue aprendiendo y mejorando en tus hábitos ecológicos.")

import random
from discord.ext import commands
from io import BytesIO
import aiohttp

@bot.command()
async def tacho_basura(ctx):
    # Lista de imágenes de residuos y su correspondiente tacho de color
    residuos = [
        {"nombre": "Plástico", "imagen_url": "img\images (1).jpeg", "tacho": "amarillo"},
        {"nombre": "Papel", "imagen_url": "img\descarga_4.jpeg", "tacho": "azul"},
        {"nombre": "Vidrio", "imagen_url": "img\descarga (2).jpeg", "tacho": "verde"},
        {"nombre": "Orgánico", "imagen_url": "img\descarga (1).jpeg", "tacho": "marrón"},
        {"nombre": "Restos no reciclables", "imagen_url": "img\images (2).jpeg", "tacho": "rojo"}
    ]

    # Escoger un residuo aleatorio
    residuo = random.choice(residuos)

    # Enviar la imagen al canal
    async with aiohttp.ClientSession() as session:
        async with session.get(residuo["imagen_url"]) as resp:
            img_data = BytesIO(await resp.read())
            await ctx.send(f"🔄 **¿En qué tacho de basura va este residuo?**\nEscribe el nombre del tacho correspondiente:\n\n🟡 Amarillo - Plásticos\n🔵 Azul - Papel\n🟢 Verde - Vidrio\n🟤 Marrón - Orgánico\n🟥 Rojo - Restos no reciclables", file=discord.File(img_data, filename="residuo.jpg"))

    # Esperar la respuesta del usuario
    def check(m):
        return m.author == ctx.author and m.content.lower() in ["amarillo", "azul", "verde", "marrón", "rojo"]

    try:
        respuesta = await bot.wait_for('message', check=check, timeout=30.0)

        if respuesta.content.lower() == residuo["tacho"]:
            await ctx.send(f"✅ ¡Correcto! El residuo de **{residuo['nombre']}** debe ir al tacho **{respuesta.content.capitalize()}**. +20 puntos. ♻️")
        else:
            await ctx.send(f"❌ ¡Incorrecto! El residuo de **{residuo['nombre']}** debe ir al tacho **{residuo['tacho'].capitalize()}**. -10 puntos. 🚮")

    except:
        await ctx.send(f"⏰ ¡Se agotó el tiempo! El residuo de **{residuo['nombre']}** va al tacho **{residuo['tacho'].capitalize()}**.")

@bot.command()
async def encuesta_ecologica(ctx):
    # Preguntas y respuestas posibles
    preguntas = [
        {"pregunta": "¿Reciclas en casa?", "respuestas": ["Sí", "No"], "puntos": {"Sí": 10, "No": -5}},
        {"pregunta": "¿Usas transporte público o bicicleta en lugar de automóvil?", "respuestas": ["Sí", "No"], "puntos": {"Sí": 15, "No": -10}},
        {"pregunta": "¿Apagas las luces y electrodomésticos cuando no los usas?", "respuestas": ["Sí", "No"], "puntos": {"Sí": 10, "No": -5}},
        {"pregunta": "¿Compras productos orgánicos y de comercio justo?", "respuestas": ["Sí", "No"], "puntos": {"Sí": 15, "No": -5}},
        {"pregunta": "¿Has instalado tecnologías sostenibles en tu hogar (como paneles solares)?", "respuestas": ["Sí", "No"], "puntos": {"Sí": 20, "No": -10}},
        {"pregunta": "¿Evitas el uso de plásticos de un solo uso?", "respuestas": ["Sí", "No"], "puntos": {"Sí": 15, "No": -5}},
        {"pregunta": "¿Tienes una planta o jardín en casa?", "respuestas": ["Sí", "No"], "puntos": {"Sí": 10, "No": -5}}
    ]
    
    puntos_totales = 0

    # Iterar sobre las preguntas y obtener las respuestas
    for pregunta in preguntas:
        await ctx.send(f"❓ **{pregunta['pregunta']}**\nResponde con: `Sí` o `No`")

        def check(m):
            return m.author == ctx.author and m.content in ["Sí", "No"]

        try:
            respuesta = await bot.wait_for('message', check=check, timeout=30.0)

            if respuesta.content == "Sí":
                puntos_totales += pregunta["puntos"]["Sí"]
                await ctx.send(f"✅ ¡Gracias por tu respuesta! +{pregunta['puntos']['Sí']} puntos.")
            else:
                puntos_totales += pregunta["puntos"]["No"]
                await ctx.send(f"❌ ¡Gracias por tu respuesta! -{pregunta['puntos']['No']} puntos.")
        except:
            await ctx.send("⏰ ¡Se agotó el tiempo para responder!")

    # Resultado final
    if puntos_totales > 80:
        await ctx.send(f"🌟 ¡Eres un verdadero ecologista! Has obtenido {puntos_totales} puntos. Sigue así y el planeta te lo agradecerá. 🌍")
    elif puntos_totales > 40:
        await ctx.send(f"🌱 ¡Lo estás haciendo bien! Has obtenido {puntos_totales} puntos. Aún hay más por hacer. ¡Sigue aprendiendo y mejorando! 🌏")
    else:
        await ctx.send(f"⚠️ ¡Tu puntaje es de {puntos_totales} puntos! Es hora de mejorar tus hábitos ecológicos. ¡Cada pequeño esfuerzo cuenta! 🌍")

@bot.command()
async def desafio_comida(ctx):
    # Preguntas y respuestas posibles sobre alimentos sostenibles
    preguntas = [
        {"pregunta": "¿Prefieres comprar alimentos locales y de temporada?", "respuestas": ["Sí", "No"], "puntos": {"Sí": 15, "No": -5}},
        {"pregunta": "¿Consumes productos orgánicos en tu alimentación?", "respuestas": ["Sí", "No"], "puntos": {"Sí": 20, "No": -10}},
        {"pregunta": "¿Has reducido el consumo de alimentos de origen animal?", "respuestas": ["Sí", "No"], "puntos": {"Sí": 25, "No": -15}},
        {"pregunta": "¿Evitas los productos empaquetados en plástico?", "respuestas": ["Sí", "No"], "puntos": {"Sí": 20, "No": -10}},
        {"pregunta": "¿Prefieres alimentos con menos empaque o en envases reutilizables?", "respuestas": ["Sí", "No"], "puntos": {"Sí": 15, "No": -5}},
        {"pregunta": "¿Estás dispuesto a probar alternativas vegetales a la carne?", "respuestas": ["Sí", "No"], "puntos": {"Sí": 25, "No": -15}},
        {"pregunta": "¿Reutilizas o compostas los restos de comida?", "respuestas": ["Sí", "No"], "puntos": {"Sí": 20, "No": -10}}
    ]

    puntos_totales = 0

    # Iterar sobre las preguntas y obtener las respuestas
    for pregunta in preguntas:
        await ctx.send(f"❓ **{pregunta['pregunta']}**\nResponde con: `Sí` o `No`")

        def check(m):
            return m.author == ctx.author and m.content in ["Sí", "No"]

        try:
            respuesta = await bot.wait_for('message', check=check, timeout=30.0)

            if respuesta.content == "Sí":
                puntos_totales += pregunta["puntos"]["Sí"]
                await ctx.send(f"✅ ¡Excelente elección! +{pregunta['puntos']['Sí']} puntos.")
            else:
                puntos_totales += pregunta["puntos"]["No"]
                await ctx.send(f"❌ ¡Gracias por tu respuesta! -{pregunta['puntos']['No']} puntos.")
        except:
            await ctx.send("⏰ ¡Se agotó el tiempo para responder!")

    # resultado final
    if puntos_totales > 130:
        await ctx.send(f"🌍 ¡Eres un verdadero defensor de la comida sostenible! Has obtenido {puntos_totales} puntos. ¡Continúa promoviendo la sostenibilidad en tu alimentación! 🌱")
    elif puntos_totales > 70:
        await ctx.send(f"🌱 ¡Buen trabajo! Has obtenido {puntos_totales} puntos. Aún puedes hacer más para mejorar tus hábitos alimenticios sostenibles. 🍴")
    else:
        await ctx.send(f"⚠️ ¡Tu puntaje es de {puntos_totales} puntos! Es hora de tomar decisiones más sostenibles. ¡Tu alimentación también puede ser parte de la solución! 🌍")
@bot.command()
async def desafio_clima(ctx):
    # Afirmaciones sobre el cambio climático
    afirmaciones = [
        {"afirmacion": "El aumento de la temperatura global está provocando el derretimiento de los glaciares en los polos.", "respuesta_correcta": "Sí"},
        {"afirmacion": "Las sequías prolongadas no están relacionadas con el cambio climático.", "respuesta_correcta": "No"},
        {"afirmacion": "El cambio climático aumenta la frecuencia de fenómenos meteorológicos extremos como huracanes y tormentas.", "respuesta_correcta": "Sí"},
        {"afirmacion": "La deforestación contribuye al cambio climático al reducir la cantidad de árboles que capturan CO2.", "respuesta_correcta": "Sí"},
        {"afirmacion": "Las emisiones de gases de efecto invernadero solo provienen de los sectores industriales y no de la agricultura.", "respuesta_correcta": "No"},
        {"afirmacion": "El cambio climático está afectando la biodiversidad, poniendo en peligro muchas especies animales.", "respuesta_correcta": "Sí"},
        {"afirmacion": "La energía solar no es una fuente renovable, por lo tanto contribuye al cambio climático.", "respuesta_correcta": "No"}
    ]
    
    puntuacion = 0
    
    for afirmacion in afirmaciones:
        await ctx.send(f"❓ **{afirmacion['afirmacion']}**\nResponde con: `Sí` o `No`")
        
        def check(m):
            return m.author == ctx.author and m.content in ["Sí", "No"]
        
        try:
            respuesta = await bot.wait_for('message', check=check, timeout=30.0)
            
            if respuesta.content == afirmacion["respuesta_correcta"]:
                puntuacion += 10
                await ctx.send(f"✅ ¡Correcto! +10 puntos.")
            else:
                await ctx.send(f"❌ Incorrecto. La respuesta correcta es `{afirmacion['respuesta_correcta']}`.")
        
        except:
            await ctx.send("⏰ ¡Se agotó el tiempo para responder!")
    
    # Resultado final
    if puntuacion >= 50:
        await ctx.send(f"🌍 ¡Increíble! Has obtenido {puntuacion} puntos. ¡Estás muy informado sobre el cambio climático y sus efectos!")
    elif puntuacion >= 30:
        await ctx.send(f"🌱 Buen trabajo, has obtenido {puntuacion} puntos. ¡Sigue aprendiendo sobre el cambio climático!")
    else:
        await ctx.send(f"⚠️ Tu puntuación es de {puntuacion} puntos. ¡Es importante estar más informado sobre el cambio climático y sus efectos!")

@bot.command()
async def check(ctx):
    if ctx.message.attachments:
        for attachments in ctx.message.attachments:
            file_name = attachments.filename
            file_url = attachments.url
            await attachments.save(f"./{attachments.filename}")
            
            # Obtener la clasificación desde el modelo
            classification_result = get_class(
                model_path="./keras_model.h5",
                labels_path="labels.txt",
                image_paht=f"./{attachments.filename}"
            )
            
            # Extraer la clase desde el resultado
            class_name = classification_result.split(",")[0].replace("Clase:", "").strip()
            
            # Mapeo de emojis según el tacho
            emoji_mapping = {
                "Tacho Verde": "🟩",  # Tacho verde
                "Tacho Rojo": "🟥",   # Tacho rojo
                "Tacho Marrón": "🟫", # Tacho marrón
                "Tacho Azul": "🟦",   # Tacho azul
                "Tacho Amarillo": "🟨",# Tacho amarillo
            }
            
            # Construir el mensaje con el emoji y el tacho
            emoji = emoji_mapping.get(class_name, "❓")
            response_message = (
                f"🚮 Clasificación: **{class_name}** {emoji}\n"
                f"📥 ¡Por favor deposita este residuo en el tacho adecuado! 🌱"
            )
            
            # Enviar el mensaje al usuario
            await ctx.send(response_message)
    else:
        await ctx.send("❌ Oh no, no has subido ninguna foto. Por favor, sube una imagen para clasificar.")

@bot.command()
async def help(ctx):
    """Muestra una lista de comandos disponibles con descripciones."""
    ayuda = (
        "🌍 **Lista de comandos disponibles:**\n\n"
        "✨ **Comandos generales:**\n"
        "  - 📜 `/datocurioso` - Recibe un dato curioso sobre la contaminación.\n"
        "  - 🧠 `/quiz` - Inicia un minijuego de preguntas para aprender más.\n"
        "  - 🎮 `/aventura` - Participa en una aventura interactiva para salvar el planeta.\n"
        "  - 💡 `/adivina` - Juega a adivinar palabras relacionadas con ecología.\n\n"
        "♻️ **Comandos de reciclaje y residuos:**\n"
        "  - 🖼️ `/check` - Clasifica residuos subiendo una imagen y obteniendo el tacho correcto.\n"
        "  - 🗑️ `/tacho_basura` - Aprende a clasificar residuos con imágenes interactivas.\n\n"
        "🌱 **Comandos educativos y de reflexión:**\n"
        "  - 🌟 `/sabio_ecologico` - Responde preguntas para ganar sabiduría ecológica.\n"
        "  - 📖 `/diario_ecologico` - Registra acciones ecológicas diarias y acumula puntos.\n"
        "  - 🍴 `/desafio_comida` - Responde preguntas sobre prácticas alimenticias sostenibles.\n"
        "  - 🌡️ `/desafio_clima` - Evalúa tus conocimientos sobre cambio climático.\n"
        "  - 📊 `/encuesta_ecologica` - Contesta preguntas sobre tus hábitos ecológicos.\n\n"
        "✨ Usa estos comandos para interactuar con Ecobot y aprender más sobre cómo cuidar el planeta. ¡Cada acción cuenta! 🌎\n"
    )
    await ctx.send(ayuda)

bot.run('MTMxMjQ5NDAzMjI4NjY0NjM3Mw.GUKLRM.IDKb8vsNWeCMw9zfvCJQanUFLVaGPAim5iUzHg')