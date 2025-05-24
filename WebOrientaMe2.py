import streamlit as st
import pandas as pd
import os
import json


st.set_page_config(page_title="OrientaMe+", layout="centered")

# Página de lobby (introducción y nombre)
def mostrar_lobby():
    st.title("🌟 Bienvenido a OrientaMe")
    st.write("OrientaMe es una herramienta educativa que te ayuda a explorar tus intereses académicos y profesionales para tomar mejores decisiones sobre tu futuro.")
    st.write("A través de tus puntajes ICFES, intereses y fortalezas, te recomendamos carreras y te brindamos información relevante para tu orientación vocacional.")
    st.markdown("---")
    nombre = st.text_input("Ingresa tu nombre para comenzar:", value=st.session_state.nombre_usuario)
    if len(nombre.strip()) >= 3:
        st.session_state.nombre_usuario = nombre
        if st.button("Ingresar a la plataforma"):
            st.session_state.pagina = 'inicio'
          
# Página de inicio
# Ruta del archivo donde se guardarán las reseñas
RESEÑAS_FILE = "reseñas.json"

# Cargar reseñas desde archivo si existe
if os.path.exists(RESEÑAS_FILE):
    try:
        with open(RESEÑAS_FILE, "r", encoding="utf-8") as f:
            contenido = f.read().strip()
            if contenido:
                f.seek(0)
                reseñas_guardadas = json.load(f)
            else:
                raise ValueError("Archivo vacío")
    except (json.JSONDecodeError, ValueError):
        reseñas_guardadas = [
            "\"Muy útil para entender qué estudiar.\" — Ana",
            "\"Me ayudó a decidir entre medicina y biología.\" — Juan",
            "\"Fácil de usar y bien organizado.\" — Laura"
        ]
else:
    reseñas_guardadas = [
        "\"Muy útil para entender qué estudiar.\" — Ana",
        "\"Me ayudó a decidir entre medicina y biología.\" — Juan",
        "\"Fácil de usar y bien organizado.\" — Laura"
    ]

# Inicializar el estado de navegación y reseñas si no existen
if 'pagina' not in st.session_state:
    st.session_state.pagina = 'lobby'
if 'reseñas' not in st.session_state:
    st.session_state.reseñas = reseñas_guardadas

# Guardar reseñas actuales al archivo
with open(RESEÑAS_FILE, "w", encoding="utf-8") as f:
    json.dump(st.session_state.reseñas, f, ensure_ascii=False, indent=2)


def mostrar_inicio():
    st.title(f"🎓 Bienvenido a OrientaMe+ (Versión Avanzada), {st.session_state.nombre_usuario}!")
    st.subheader("Sumérgete en esta aventura para descubrir tu camino profesional")
    st.subheader("¿Qué deseas hacer?")
    col1, col2 = st.columns(2)
    with col1:
        if st.button("🔍 Buscar una carrera"):
            st.session_state.pagina = 'buscar'
    with col2:
        if st.button("💡 Ver consejos"):
            st.session_state.pagina = 'consejos'

def mostrar_consejos():
    st.title("💡 Consejos")
    tema = st.selectbox("Selecciona un tema para ver consejos:",["Seleccionar", "Carreras"] )
    if tema == "Carreras":
        carrera = st.selectbox(
            "Seleccionar la carrera que te interese:",
            ["Seleccionar", "Ingeniería Industrial", "Ingeniería de Sistemas", "Ingeniería Eléctrica", "Ingeniería Electrónica", "Diseño Industrial", "Enfermería", "Fisioterapia", "Derecho", "Contaduría Pública", "Administración de Empresas", "Psicología", "Trabajo Social", "Ingeniería Civil", "Ingeniería Mecánica", "Ingeniería Ambiental" ]
        )
        
        if carrera:
             info_carreras = {
                "Ingeniería Industrial": {
                 "a": "Aprende Excel y herramientas de análisis desde temprano.",
                 "b": "Familiarízate con metodologías como Lean, Six Sigma y simulación.",
                 "c": "Desarrolla habilidades blandas (liderazgo, comunicación, trabajo en equipo).",
                 "d": "Realiza prácticas o proyectos en empresas reales cuanto antes."
            },
                "Ingeniería de Sistemas": {
                 "a": "Domina los fundamentos: algoritmos, estructuras de datos y lógica.",
                 "b": "Practica constantemente con proyectos personales o freelance.",
                 "c": "Aprende inglés técnico y plataformas como GitHub.",
                 "d": "Mantente actualizado en nuevas tecnologías (IA, blockchain, etc.)."
            },
                 "Ingeniería Eléctrica": {
                 "a": "Refuerza tu base en matemáticas y física.",
                 "b": "Aprende a usar simuladores como MATLAB, Proteus o PSpice.",
                 "c": "Realiza laboratorios con atención al detalle.",
                 "d": "Participa en semilleros o proyectos energéticos."
            },
                 "Ingeniería Electrónica": {
                 "a": "Refuerza conocimientos en circuitos y programación de microcontroladores (Arduino, ESP32).",
                 "b": "Participa en clubes de robótica o electrónica.",
                 "c": "Documenta todos tus proyectos y prácticas.",
                 "d": "Relaciónate con estudiantes de otras ramas (sistemas, eléctrica)."
            },
                 "Diseño Industrial": {
                 "a": "Aprende a usar software como Rhino, SolidWorks, Illustrator y AutoCAD.",
                 "b": "Crea portafolios desde primer semestre.",
                 "c": "Sé curioso: estudia tendencias, formas, materiales y ergonomía.",
                 "d": "Participa en concursos o ferias de diseño."
            },
                "Enfermería": {
                 "a": "Desarrolla empatía y habilidades de comunicación con pacientes.",
                 "b": "Organiza tu tiempo para prácticas clínicas, que suelen ser exigentes.",
                 "c": "Mantente actualizado en protocolos de bioseguridad y primeros auxilios. ",
                 "d": "Busca mentoría de enfermeros experimentados."
            },
                 "Fisioterapia": {
                 "a": "Estudia bien la anatomía y biomecánica.",
                 "b": "Cuida tu postura y salud física: tu cuerpo es tu herramienta.",
                 "c": "Participa en voluntariados en fundaciones o clubes deportivos.",
                 "d": "Aprende técnicas manuales y manejo de equipos desde temprano."
            },
                 "Derecho": {
                 "a": "Desarrolla lectura crítica y capacidad de argumentación.",
                 "b": "Aprende a escribir bien: los textos jurídicos deben ser precisos.",
                 "c": "Estudia con códigos y constitución en mano.",
                 "d": "Participa en simulacros de audiencias o grupos de debate."
            },
                 "Contaduría Pública": {
                 "a":"Practica contabilidad desde primer semestre (usa software contable).",
                 "b": "Aprende normativas como NIIF y manejo tributario colombiano.",
                 "c": "Estudia casos reales y lleva tus propias cuentas.",
                 "d": "Sé muy organizado con tu documentación."
            },
                 "Administración de Empresas": {
                 "a": "Fomenta pensamiento estratégico y toma de decisiones.",
                 "b": "Aprende sobre liderazgo, marketing, finanzas y emprendimiento.",
                 "c": "Participa en ferias empresariales o crea tu microempresa.",
                 "d": "Aprovecha materias electivas para especializarte."
            },
                 "Psicología": {
                 "a": "Cuida tu salud mental desde el inicio.",
                 "b": "Estudia con base en casos reales y entrevistas.",
                 "c": "Participa en prácticas sociales o clínicas cuando puedas.",
                 "d": "Investiga sobre neurociencia y psicometría."
            },
                 "Trabajo Social": {
                 "a": "Desarrolla habilidades comunicativas y escucha activa.",
                 "b": "Involúcrate en procesos comunitarios desde los primeros semestres.",
                 "c": "Aprende sobre políticas públicas y legislación social.",
                 "d": "Ten apertura a contextos sociales diversos."
            },
                 "Ingeniería Civil": {
                 "a": "Aprende AutoCAD, Civil 3D, SAP2000, y herramientas de diseño estructural",
                 "b": "Asiste a obras y practica levantamientos topográficos.",
                 "c": "Cuida la ética en temas de licitaciones y presupuestos.",
                 "d": "Aprende a trabajar bajo presión y en campo."
            },
                 "Ingeniería Mecánica": {
                 "a": "Refuerza física, termodinámica, y mecánica de materiales.",
                 "b": "Aprende SolidWorks, Inventor, MATLAB, y simulaciones por elementos finitos.",
                 "c": "Participa en proyectos como diseño de autos o máquinas.",
                 "d": "Asegúrate de entender los procesos de manufactura."
            },
                 "Ingeniería Ambiental": {
                 "a": "Aprende sobre legislación ambiental colombiana.",
                 "b": "Participa en proyectos de reciclaje, cuidado del agua, o reforestación.",
                 "c": "Refuerza química, microbiología, y procesos de tratamiento.",
                 "d": "Apóyate en GIS y software como ArcGIS o HEC-RAS."
            }
        }
        st.markdown(f"Has seleccionado la carrera **{carrera}**")
        st.write(f"- {info_carreras.get(carrera, {}).get('a', 'Informacion no disponible')}")
        st.write(f"- {info_carreras.get(carrera, {}).get('b', 'Informacion no disponible')}")
        st.write(f"- {info_carreras.get(carrera, {}).get('c', 'Informacion no disponible')}")
        st.write(f"- {info_carreras.get(carrera, {}).get('d', 'Informacion no disponible')}")


    if st.button("🎲 Consejo aleatorio"):
        import random
        consejos = [
            "Organiza tu tiempo de manera efectiva, establece prioridades y crea un calendario para cumplir con tus objetivos.",
            "No tengas miedo de preguntar, la participación activa en clases es clave para entender los conceptos y demostrar tu interés.",
            "Aprovecha los recursos universitarios, como bibliotecas, laboratorios y tutorías, para mejorar tu aprendizaje y rendimiento.",
            "Cuida tu salud física y mental, come bien, haz ejercicio regularmente y busca ayuda si necesitas apoyo emocional.",
            "Establece metas claras y alcanzables, tanto a corto como a largo plazo, y trabaja hacia ellas de manera consistente.",
            "Sé flexible y adaptable, la vida universitaria puede ser impredecible, pero con una actitud positiva y resiliente, podrás superar cualquier obstáculo.",
            "Aprende de tus errores, no te desanimes por los fracasos, sino que utilízalos como oportunidades para crecer y mejorar.",
            "Mantén una actitud positiva y enfócate en las oportunidades que te brinda la universidad, aprovecha al máximo tu tiempo y recursos.",
            "Desarrolla habilidades blandas, como la comunicación efectiva, el trabajo en equipo y la resolución de problemas, que te serán útiles en tu vida profesional.",
            "No te aísles, conecta con tus compañeros y profesores, y aprovecha las oportunidades para establecer redes de contactos y apoyo."

        ]
        st.success(random.choice(consejos))

    if st.button("⬅️ Volver al inicio"):
        st.session_state.pagina = 'inicio'

def calcular_probabilidad(icfes, corte):
    if corte == 0:
        return "No disponible"
    elif icfes >= corte + 3:
        return "🎯 Muy altas"
    elif icfes >= corte + 1.5:
        return "✅ Altas"
    elif icfes >= corte - 1.5:
        return "🟡 Medias"
    elif icfes >= corte - 3:
        return "🔻 Bajas"
    else:
        return "❌ Muy bajas"


def mostrar_busqueda():
    st.title("🔍 Orientador de Carreras Personalizado")

    st.header(f"Ingrese los siguiente datos {st.session_state.nombre_usuario}")
    edad = st.number_input("Edad:", min_value=14, max_value=99, value=18)
    universidad = st.selectbox("Universidad a postularse:", ["UIS", "UTS", "SENA",])
    fortalezas = st.multiselect("Áreas en las que te sientes fuerte:", ["Matemáticas", "Comunicación", "Biología", "Arte", "Liderazgo", "Tecnología"])
    

    st.header("Puntajes ICFES")
    mates = st.number_input("Matemáticas:", 0, 100, 50)
    ingles = st.number_input("Inglés:", 0, 100, 50)
    lectura = st.number_input("Lectura Crítica:", 0, 100, 50)
    sociales = st.number_input("Sociales y Ciudadanas:", 0, 100, 50)
    ciencias = st.number_input("Ciencias Naturales:", 0, 100, 50)
    icfes_total = mates + ingles + lectura + sociales + ciencias
    st.markdown(f"**Puntaje ICFES Total:** {icfes_total}")

    intereses = st.multiselect("Áreas de interés:", ["Tecnología", "Arte", "Salud", "Educación", "Negocios", "Ciencia"])

    if st.button("🔎 Obtener recomendaciones"):
         # Diccionario de áreas de interés por carrera
        intereses_por_carrera = {
            "Ingeniería Industrial": ["Negocios", "Ciencia"],
            "Ingeniería de Sistemas": ["Tecnología", "Ciencia"],
            "Ingeniería Eléctrica": ["Ciencia", "Tecnología"],
            "Ingeniería Electrónica": ["Ciencia", "Tecnología"],
            "Diseño Industrial": ["Arte", "Tecnología"],
            "Enfermería": ["Salud"],
            "Fisioterapia": ["Salud"],
            "Derecho": ["Educación"],
            "Contaduría Pública": ["Negocios"],
            "Administración de Empresas": ["Negocios"],
            "Psicología": ["Educación", "Salud"],
            "Trabajo Social": ["Educación"],
            "Ingeniería Civil": ["Ciencia"],
            "Ingeniería Mecánica": ["Ciencia"],
            "Ingeniería Ambiental": ["Ciencia"]
        }

        puntajes_base = {
            "Ingeniería Industrial": (0.25, 0.20, 0.25, 0.15, 0.15, 69.52),
            "Ingeniería de Sistemas": (0.25, 0.20, 0.35, 0.10, 0.10, 68.96),
            "Ingeniería Eléctrica": (0.30, 0.20, 0.30, 0.10, 0.10, 65.03),
            "Ingeniería Electrónica": (0.30, 0.20, 0.30, 0.10, 0.10, 66.12),
            "Diseño Industrial": (0.10, 0.20, 0.50, 0.10, 0.10, 68.19),
            "Enfermería": (0.30, 0.20, 0.15, 0.20, 0.15, 70.64),
            "Fisioterapia": (0.40, 0.20, 0.15, 0.15, 0.10, 69.62),
            "Derecho": (0.10, 0.40, 0.20, 0.20, 0.10, 69.62),
            "Contaduría Pública": (0.20, 0.25, 0.30, 0.15, 0.10, 0),
            "Administración de Empresas": (0.20, 0.25, 0.30, 0.15, 0.10, 0),
            "Psicología": (0.30, 0.30, 0.20, 0.10, 0.10, 0),
            "Trabajo Social": (0.10, 0.40, 0.10, 0.30, 0.10, 65.80),
            "Ingeniería Civil": (0.30, 0.20, 0.30, 0.10, 0.10, 70.57),
            "Ingeniería Mecánica": (0.30, 0.10, 0.40, 0.10, 0.10, 67.77),
            "Ingeniería Ambiental": (0.30, 0.25, 0.25, 0.10, 0.10, 0)
        }

        resultados = []
        for carrera, pesos in puntajes_base.items():
            puntaje = ciencias * pesos[0] + lectura * pesos[1] + mates * pesos[2] + sociales * pesos[3] + ingles * pesos[4]
            if any(i in intereses for i in intereses_por_carrera.get(carrera, [])):
                puntaje += 20
            if icfes_total >= pesos[5] and pesos[5] > 0:
                puntaje += 15
            probabilidad = calcular_probabilidad(icfes_total / 5, pesos[5])
            resultados.append((carrera, puntaje, probabilidad))
        
    
        df = pd.DataFrame(resultados, columns=['Carrera', 'Puntaje', 'Probabilidad'])
        df = df.sort_values(by="Puntaje", ascending=False).set_index('Carrera')

        st.subheader("🔝 Carreras recomendadas")
        import altair as alt
        chart = alt.Chart(df.reset_index().head(5)).mark_bar(cornerRadiusTopLeft=5, cornerRadiusTopRight=5).encode(
            x=alt.X('Carrera:N', sort='-y', title='Carrera'),
            y=alt.Y('Puntaje:Q', title='Puntaje Total'),
            color=alt.Color('Carrera:N', legend=None),
            tooltip=['Carrera', 'Puntaje', 'Probabilidad']
        ).properties(
            title='Top 5 Carreras Recomendadas',
            width=600,
            height=400
        )
        st.altair_chart(chart, use_container_width=True)
        st.table(df.head(5))

        seleccion = st.selectbox("Selecciona una carrera para más información:", df.head(5).index)
        if seleccion:
            info_carreras = {
                "Ingeniería Industrial": {
                    "Asignaturas": "Matemáticas, física, estadística, investigación de operaciones, gestión de la producción, logística, calidad, finanzas, ingeniería económica, gestión del talento humano.",
                    "Entornos": "Empresas manufactureras, consultorías, logística, calidad, producción, gestión de proyectos, emprendimiento.",
                    "Posgrados": "Maestría en Ingeniería Industrial, MBA, especializaciones en logística, calidad, gestión de proyectos."
                },
                "Ingeniería de Sistemas": {
                    "Asignaturas": "Programación, estructuras de datos, bases de datos, redes, sistemas operativos, inteligencia artificial, desarrollo de software, seguridad informática.",
                    "Entornos": "Desarrollo de software, análisis de sistemas, administración de bases de datos, ciberseguridad, consultoría tecnológica.",
                    "Posgrados": "Maestría en Ingeniería de Sistemas, especializaciones en seguridad informática, inteligencia artificial, gestión de tecnologías de la información."
                },
                "Ingeniería Eléctrica": {
                    "Asignaturas": "Circuitos eléctricos, máquinas eléctricas, sistemas de potencia, electrónica, control automático, energías renovables.",
                    "Entornos": "Empresas de energía, diseño y mantenimiento de sistemas eléctricos, automatización industrial, consultoría.",
                    "Posgrados": "Maestría en Ingeniería Eléctrica, especializaciones en energías renovables, sistemas de potencia."
                },
                "Ingeniería Electrónica": {
                    "Asignaturas": "Electrónica analógica y digital, microcontroladores, sistemas embebidos, telecomunicaciones, instrumentación.",
                    "Entornos": "Diseño y mantenimiento de sistemas electrónicos, telecomunicaciones, automatización, investigación y desarrollo.",
                    "Posgrados": "Maestría en Ingeniería Electrónica, especializaciones en telecomunicaciones, sistemas embebidos."
                },
                "Diseño Industrial": {
                    "Asignaturas": "Dibujo técnico, ergonomía, materiales, procesos de fabricación, diseño asistido por computador (CAD), gestión de proyectos.",
                    "Entornos": "Diseño de productos, mobiliario, empaques, consultoría en diseño, investigación y desarrollo.",
                    "Posgrados": "Maestría en Diseño Industrial, especializaciones en diseño de productos, diseño sostenible."
                },
                "Enfermería": {
                    "Asignaturas": "Anatomía, fisiología, farmacología, cuidados de enfermería, salud comunitaria, gestión en salud.",
                    "Entornos": "Hospitales, clínicas, centros de salud, salud pública, docencia, investigación.",
                    "Posgrados": "Maestría en Enfermería, especializaciones en cuidado crítico, salud comunitaria, administración en salud."
                },
                "Fisioterapia": {
                    "Asignaturas": "Anatomía, fisiología, kinesiología, técnicas de rehabilitación, fisioterapia deportiva, salud comunitaria.",
                    "Entornos": "Clínicas de rehabilitación, hospitales, centros deportivos, salud ocupacional, investigación.",
                    "Posgrados": "Maestría en Fisioterapia, especializaciones en fisioterapia deportiva, neurorehabilitación."
                },
                "Derecho": {
                    "Asignaturas": "Derecho civil, penal, constitucional, administrativo, laboral, internacional, teoría del derecho.",
                    "Entornos": "Abogacía, judicatura, asesoría legal, notariado, docencia, investigación.",
                    "Posgrados": "Maestría en Derecho, especializaciones en derecho penal, civil, administrativo, constitucional."
                },
                "Contaduría Pública": {
                    "Asignaturas": "Contabilidad financiera, auditoría, impuestos, finanzas, costos, ética profesional.",
                    "Entornos": "Empresas privadas, firmas de auditoría, entidades gubernamentales, consultoría financiera.",
                    "Posgrados": "Maestría en Contaduría, especializaciones en auditoría, tributación, finanzas."
                },
                "Administración de Empresas": {
                    "Asignaturas": "Economía, finanzas, marketing, recursos humanos, estrategia empresarial, emprendimiento.",
                    "Entornos": "Empresas privadas, consultorías, emprendimientos, sector público, organizaciones sin ánimo de lucro.",
                    "Posgrados": "Maestría en Administración (MBA), especializaciones en marketing, finanzas, gestión de proyectos."
                },
                "Psicología": {
                    "Asignaturas": "Psicología general, psicología clínica, psicología organizacional, neuropsicología, investigación psicológica.",
                    "Entornos": "Clínicas, hospitales, empresas, instituciones educativas, investigación.",
                    "Posgrados": "Maestría en Psicología, especializaciones en psicología clínica, organizacional, educativa."
                },
                "Comunicación Social": {
                    "Asignaturas": "Periodismo, comunicación organizacional, producción audiovisual, teoría de la comunicación, investigación.",
                    "Entornos": "Medios de comunicación, agencias de publicidad, departamentos de comunicación, consultorías.",
                    "Posgrados": "Maestría en Comunicación, especializaciones en comunicación digital, periodismo, comunicación organizacional."
                },
                "Ingeniería Civil": {
                    "Asignaturas": "Mecánica de suelos, estructuras, hidráulica, vías, construcción, gestión de proyectos.",
                    "Entornos": "Empresas constructoras, consultorías, entidades gubernamentales, supervisión de obras.",
                    "Posgrados": "Maestría en Ingeniería Civil, especializaciones en estructuras, geotecnia, hidráulica."
                },
                "Ingeniería Mecánica": {
                    "Asignaturas": "Termodinámica, mecánica de fluidos, diseño mecánico, materiales, sistemas térmicos.",
                    "Entornos": "Industria manufacturera, diseño de maquinaria, mantenimiento industrial, consultorías.",
                    "Posgrados": "Maestría en Ingeniería Mecánica, especializaciones en diseño mecánico, energía."
                },
                "Ingeniería Ambiental": {
                    "Asignaturas": "Ecología, gestión ambiental, tratamiento de aguas, residuos sólidos, evaluación de impacto ambiental.",
                    "Entornos": "Empresas de consultoría ambiental, entidades gubernamentales, ONGs, industrias.",
                    "Posgrados": "Maestría en Ingeniería Ambiental, especializaciones en gestión ambiental, tratamiento de aguas."
                }
            }
            st.markdown(f"### Información sobre **{seleccion}**")
            st.write("- Duración: 10 semestres")
            st.write(f"- Asignaturas principales: {info_carreras.get(seleccion, {}).get('Asignaturas', 'Información no disponible')}")
            st.write(f"- Entornos laborales post-carrera: {info_carreras.get(seleccion, {}).get('Entornos', 'Información no disponible')}")
            st.write(f"- Opciones de posgrado: {info_carreras.get(seleccion, {}).get('Posgrados', 'Información no disponible')}")
            st.write(f"- 📊 **Probabilidad de ingreso:** {df.loc[seleccion, 'Probabilidad']}")

    if st.button("⬅️ Volver al inicio"):
        st.session_state.pagina = 'inicio'

# Información en el sidebar
st.sidebar.info("OrientaMe - Proyecto universitario | Hecho con Streamlit")

# Sección de reseñas en el sidebar
st.sidebar.markdown("---")
st.sidebar.header("📝 Reseñas")
for reseña in st.session_state.reseñas:
    st.sidebar.write(reseña)

# Formulario para que el usuario agregue una nueva reseña
txt = st.sidebar.text_input("Escribe tu reseña aquí")
if st.sidebar.button("Agregar reseña"):
    if txt:
        st.session_state.reseñas.append(f"\"{txt}\" — {st.session_state.nombre_usuario if st.session_state.nombre_usuario else 'Usuario'}")
        with open(RESEÑAS_FILE, "w", encoding="utf-8") as f:
            json.dump(st.session_state.reseñas, f, ensure_ascii=False, indent=2)

if 'nombre_usuario' not in st.session_state:
    st.session_state.nombre_usuario = ''


if st.session_state.pagina == 'lobby':
    mostrar_lobby()
elif st.session_state.pagina == 'inicio':
    mostrar_inicio()
elif st.session_state.pagina == 'consejos':
    mostrar_consejos()
elif st.session_state.pagina == 'buscar':
    mostrar_busqueda()

  
