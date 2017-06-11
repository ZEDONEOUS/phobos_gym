--
-- PostgreSQL database dump
--

-- Dumped from database version 9.5.6
-- Dumped by pg_dump version 9.5.6

SET statement_timeout = 0;
SET lock_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SET check_function_bodies = false;
SET client_min_messages = warning;
SET row_security = off;

--
-- Name: plpgsql; Type: EXTENSION; Schema: -; Owner: 
--

CREATE EXTENSION IF NOT EXISTS plpgsql WITH SCHEMA pg_catalog;


--
-- Name: EXTENSION plpgsql; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION plpgsql IS 'PL/pgSQL procedural language';


SET search_path = public, pg_catalog;

SET default_tablespace = '';

SET default_with_oids = false;

--
-- Name: administrador; Type: TABLE; Schema: public; Owner: roguz_admin
--

CREATE TABLE administrador (
    id integer NOT NULL,
    nombre text NOT NULL,
    apellido text NOT NULL,
    usuario text NOT NULL,
    email text NOT NULL,
    contrasena text NOT NULL
);


ALTER TABLE administrador OWNER TO roguz_admin;

--
-- Name: administrador_id_seq; Type: SEQUENCE; Schema: public; Owner: roguz_admin
--

CREATE SEQUENCE administrador_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE administrador_id_seq OWNER TO roguz_admin;

--
-- Name: administrador_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: roguz_admin
--

ALTER SEQUENCE administrador_id_seq OWNED BY administrador.id;


--
-- Name: detalle_ejercicio; Type: TABLE; Schema: public; Owner: roguz_admin
--

CREATE TABLE detalle_ejercicio (
    id integer NOT NULL,
    series numeric NOT NULL,
    repeticiones numeric NOT NULL,
    nivel_dificultad character varying(1) NOT NULL,
    id_ejercicio integer NOT NULL
);


ALTER TABLE detalle_ejercicio OWNER TO roguz_admin;

--
-- Name: detalle_ejercicio_id_seq; Type: SEQUENCE; Schema: public; Owner: roguz_admin
--

CREATE SEQUENCE detalle_ejercicio_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE detalle_ejercicio_id_seq OWNER TO roguz_admin;

--
-- Name: detalle_ejercicio_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: roguz_admin
--

ALTER SEQUENCE detalle_ejercicio_id_seq OWNED BY detalle_ejercicio.id;


--
-- Name: ejercicio; Type: TABLE; Schema: public; Owner: roguz_admin
--

CREATE TABLE ejercicio (
    id integer NOT NULL,
    nombre character varying(50) NOT NULL,
    descripcion text NOT NULL
);


ALTER TABLE ejercicio OWNER TO roguz_admin;

--
-- Name: ejercicio_id_seq; Type: SEQUENCE; Schema: public; Owner: roguz_admin
--

CREATE SEQUENCE ejercicio_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE ejercicio_id_seq OWNER TO roguz_admin;

--
-- Name: ejercicio_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: roguz_admin
--

ALTER SEQUENCE ejercicio_id_seq OWNED BY ejercicio.id;


--
-- Name: rutina; Type: TABLE; Schema: public; Owner: roguz_admin
--

CREATE TABLE rutina (
    id integer NOT NULL,
    nombre character varying(50) NOT NULL,
    descripcion text NOT NULL
);


ALTER TABLE rutina OWNER TO roguz_admin;

--
-- Name: rutina_id_seq; Type: SEQUENCE; Schema: public; Owner: roguz_admin
--

CREATE SEQUENCE rutina_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE rutina_id_seq OWNER TO roguz_admin;

--
-- Name: rutina_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: roguz_admin
--

ALTER SEQUENCE rutina_id_seq OWNED BY rutina.id;


--
-- Name: rutinas_ejercicios; Type: TABLE; Schema: public; Owner: roguz_admin
--

CREATE TABLE rutinas_ejercicios (
    id integer NOT NULL,
    id_ejercicio integer NOT NULL,
    id_rutina integer NOT NULL
);


ALTER TABLE rutinas_ejercicios OWNER TO roguz_admin;

--
-- Name: rutinas_ejercicios_id_seq; Type: SEQUENCE; Schema: public; Owner: roguz_admin
--

CREATE SEQUENCE rutinas_ejercicios_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE rutinas_ejercicios_id_seq OWNER TO roguz_admin;

--
-- Name: rutinas_ejercicios_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: roguz_admin
--

ALTER SEQUENCE rutinas_ejercicios_id_seq OWNED BY rutinas_ejercicios.id;


--
-- Name: rutinas_tipos_cuerpo; Type: TABLE; Schema: public; Owner: roguz_admin
--

CREATE TABLE rutinas_tipos_cuerpo (
    id integer NOT NULL,
    id_tipo_cuerpo integer,
    id_rutina integer
);


ALTER TABLE rutinas_tipos_cuerpo OWNER TO roguz_admin;

--
-- Name: rutinas_tipos_cuerpo_id_seq; Type: SEQUENCE; Schema: public; Owner: roguz_admin
--

CREATE SEQUENCE rutinas_tipos_cuerpo_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE rutinas_tipos_cuerpo_id_seq OWNER TO roguz_admin;

--
-- Name: rutinas_tipos_cuerpo_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: roguz_admin
--

ALTER SEQUENCE rutinas_tipos_cuerpo_id_seq OWNED BY rutinas_tipos_cuerpo.id;


--
-- Name: rutinas_usuarios; Type: TABLE; Schema: public; Owner: roguz_admin
--

CREATE TABLE rutinas_usuarios (
    id integer NOT NULL,
    id_usuario integer,
    id_rutina integer
);


ALTER TABLE rutinas_usuarios OWNER TO roguz_admin;

--
-- Name: rutinas_usuarios_id_seq; Type: SEQUENCE; Schema: public; Owner: roguz_admin
--

CREATE SEQUENCE rutinas_usuarios_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE rutinas_usuarios_id_seq OWNER TO roguz_admin;

--
-- Name: rutinas_usuarios_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: roguz_admin
--

ALTER SEQUENCE rutinas_usuarios_id_seq OWNED BY rutinas_usuarios.id;


--
-- Name: tipo_cuerpo; Type: TABLE; Schema: public; Owner: roguz_admin
--

CREATE TABLE tipo_cuerpo (
    id integer NOT NULL,
    descripcion text NOT NULL
);


ALTER TABLE tipo_cuerpo OWNER TO roguz_admin;

--
-- Name: tipo_cuerpo_id_seq; Type: SEQUENCE; Schema: public; Owner: roguz_admin
--

CREATE SEQUENCE tipo_cuerpo_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE tipo_cuerpo_id_seq OWNER TO roguz_admin;

--
-- Name: tipo_cuerpo_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: roguz_admin
--

ALTER SEQUENCE tipo_cuerpo_id_seq OWNED BY tipo_cuerpo.id;


--
-- Name: usuario; Type: TABLE; Schema: public; Owner: roguz_admin
--

CREATE TABLE usuario (
    id integer NOT NULL,
    nombre text NOT NULL,
    apellido text NOT NULL,
    usuario text NOT NULL,
    email text NOT NULL,
    contrasena text NOT NULL
);


ALTER TABLE usuario OWNER TO roguz_admin;

--
-- Name: usuario_id_seq; Type: SEQUENCE; Schema: public; Owner: roguz_admin
--

CREATE SEQUENCE usuario_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE usuario_id_seq OWNER TO roguz_admin;

--
-- Name: usuario_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: roguz_admin
--

ALTER SEQUENCE usuario_id_seq OWNED BY usuario.id;


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: roguz_admin
--

ALTER TABLE ONLY administrador ALTER COLUMN id SET DEFAULT nextval('administrador_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: roguz_admin
--

ALTER TABLE ONLY detalle_ejercicio ALTER COLUMN id SET DEFAULT nextval('detalle_ejercicio_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: roguz_admin
--

ALTER TABLE ONLY ejercicio ALTER COLUMN id SET DEFAULT nextval('ejercicio_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: roguz_admin
--

ALTER TABLE ONLY rutina ALTER COLUMN id SET DEFAULT nextval('rutina_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: roguz_admin
--

ALTER TABLE ONLY rutinas_ejercicios ALTER COLUMN id SET DEFAULT nextval('rutinas_ejercicios_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: roguz_admin
--

ALTER TABLE ONLY rutinas_tipos_cuerpo ALTER COLUMN id SET DEFAULT nextval('rutinas_tipos_cuerpo_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: roguz_admin
--

ALTER TABLE ONLY rutinas_usuarios ALTER COLUMN id SET DEFAULT nextval('rutinas_usuarios_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: roguz_admin
--

ALTER TABLE ONLY tipo_cuerpo ALTER COLUMN id SET DEFAULT nextval('tipo_cuerpo_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: roguz_admin
--

ALTER TABLE ONLY usuario ALTER COLUMN id SET DEFAULT nextval('usuario_id_seq'::regclass);


--
-- Data for Name: administrador; Type: TABLE DATA; Schema: public; Owner: roguz_admin
--

COPY administrador (id, nombre, apellido, usuario, email, contrasena) FROM stdin;
1	Santiago	Silva Cartagena	admin	santiago.silcart@gmail.com	$5$rounds=535000$Vdi8FyjKnxs1fwYH$.aTpXUYXxL3129j5gJlxHMqEFx9FUIwgtSRr4xLOv9B
\.


--
-- Name: administrador_id_seq; Type: SEQUENCE SET; Schema: public; Owner: roguz_admin
--

SELECT pg_catalog.setval('administrador_id_seq', 1, true);


--
-- Data for Name: detalle_ejercicio; Type: TABLE DATA; Schema: public; Owner: roguz_admin
--

COPY detalle_ejercicio (id, series, repeticiones, nivel_dificultad, id_ejercicio) FROM stdin;
\.


--
-- Name: detalle_ejercicio_id_seq; Type: SEQUENCE SET; Schema: public; Owner: roguz_admin
--

SELECT pg_catalog.setval('detalle_ejercicio_id_seq', 1, false);


--
-- Data for Name: ejercicio; Type: TABLE DATA; Schema: public; Owner: roguz_admin
--

COPY ejercicio (id, nombre, descripcion) FROM stdin;
1	Sentadillas	Posicion de inicio, de pie\r\nTalones no mas alla de la anchura de los hombros\r\nCaderas por debajo de las rodillas\r\nLas palmas tocan los muslos
2	Flexiones	Posicion de inicio, boca abajo, codos cerca al torso, bajar hasta que el pecho toque el suelo, espalda recta
3	Abdominales	Posicion de inicio, acostado sobre el suelo boca arriba, rodillas levantadas, los pies no se levantan del suelo, elevar el torso hasta que los codos toquen las rodillas\r\n\r\nDiferentes dificultades
4	Saltos	Ejecucion de repeticiones de saltos segidos durante un limite de tiempo especifico
\.


--
-- Name: ejercicio_id_seq; Type: SEQUENCE SET; Schema: public; Owner: roguz_admin
--

SELECT pg_catalog.setval('ejercicio_id_seq', 4, true);


--
-- Data for Name: rutina; Type: TABLE DATA; Schema: public; Owner: roguz_admin
--

COPY rutina (id, nombre, descripcion) FROM stdin;
3	Ares	Rutina Avanzada
1	Loki	Rutina intermedio avanzada
9	Odin	Rutina intermedio basica
10	Zeus	Rutina avanzada
11	Ra	INtermedia
\.


--
-- Name: rutina_id_seq; Type: SEQUENCE SET; Schema: public; Owner: roguz_admin
--

SELECT pg_catalog.setval('rutina_id_seq', 11, true);


--
-- Data for Name: rutinas_ejercicios; Type: TABLE DATA; Schema: public; Owner: roguz_admin
--

COPY rutinas_ejercicios (id, id_ejercicio, id_rutina) FROM stdin;
1	1	1
2	2	1
4	1	3
5	2	3
6	3	3
13	1	10
14	3	10
15	4	10
16	2	9
17	4	9
18	4	11
\.


--
-- Name: rutinas_ejercicios_id_seq; Type: SEQUENCE SET; Schema: public; Owner: roguz_admin
--

SELECT pg_catalog.setval('rutinas_ejercicios_id_seq', 18, true);


--
-- Data for Name: rutinas_tipos_cuerpo; Type: TABLE DATA; Schema: public; Owner: roguz_admin
--

COPY rutinas_tipos_cuerpo (id, id_tipo_cuerpo, id_rutina) FROM stdin;
3	2	1
4	1	1
7	3	9
8	1	9
9	2	3
10	1	10
11	1	3
12	1	11
\.


--
-- Name: rutinas_tipos_cuerpo_id_seq; Type: SEQUENCE SET; Schema: public; Owner: roguz_admin
--

SELECT pg_catalog.setval('rutinas_tipos_cuerpo_id_seq', 12, true);


--
-- Data for Name: rutinas_usuarios; Type: TABLE DATA; Schema: public; Owner: roguz_admin
--

COPY rutinas_usuarios (id, id_usuario, id_rutina) FROM stdin;
4	4	1
5	6	10
6	3	9
7	3	3
8	7	9
9	7	10
\.


--
-- Name: rutinas_usuarios_id_seq; Type: SEQUENCE SET; Schema: public; Owner: roguz_admin
--

SELECT pg_catalog.setval('rutinas_usuarios_id_seq', 9, true);


--
-- Data for Name: tipo_cuerpo; Type: TABLE DATA; Schema: public; Owner: roguz_admin
--

COPY tipo_cuerpo (id, descripcion) FROM stdin;
1	Mesomorfo
2	Hectomorfo
3	Endomorfo
\.


--
-- Name: tipo_cuerpo_id_seq; Type: SEQUENCE SET; Schema: public; Owner: roguz_admin
--

SELECT pg_catalog.setval('tipo_cuerpo_id_seq', 3, true);


--
-- Data for Name: usuario; Type: TABLE DATA; Schema: public; Owner: roguz_admin
--

COPY usuario (id, nombre, apellido, usuario, email, contrasena) FROM stdin;
3	Miguel	Castañeda	m_cast	m_cast@gmail.com	$5$rounds=535000$03YM15xPXirUzVyT$2iuyLjl.S4y0wSD15/OaIrtJyJzcvGwxbF29yHrqktB
4	Mauricio	Silva	silk.mao	silk.mao@gmail.com	$5$rounds=535000$z.3b2NjPZeuYjeRv$2oDzD/ZxwX82bWbB0T/3ftzhXEc7FyMFGeuV9HCdMo9
6	Cesar	Pinzon	neon	neon@gmail.com	$5$rounds=535000$Ccq559sFj4CSViU7$BraBVehXfEtuCZEzcvZJsVCiHyaWBlR87nAuWHsX/W3
7	Diana	Rodrigez	diana	diana@gmail.com	$5$rounds=535000$PuBN/ecEXAY8G8W.$jhzbAesdidZv1mO3OQJM345oPWpDV3qwrJFYjPj7nH8
\.


--
-- Name: usuario_id_seq; Type: SEQUENCE SET; Schema: public; Owner: roguz_admin
--

SELECT pg_catalog.setval('usuario_id_seq', 7, true);


--
-- Name: administrador_pkey; Type: CONSTRAINT; Schema: public; Owner: roguz_admin
--

ALTER TABLE ONLY administrador
    ADD CONSTRAINT administrador_pkey PRIMARY KEY (id);


--
-- Name: detalle_ejercicio_pkey; Type: CONSTRAINT; Schema: public; Owner: roguz_admin
--

ALTER TABLE ONLY detalle_ejercicio
    ADD CONSTRAINT detalle_ejercicio_pkey PRIMARY KEY (id);


--
-- Name: ejercicio_pkey; Type: CONSTRAINT; Schema: public; Owner: roguz_admin
--

ALTER TABLE ONLY ejercicio
    ADD CONSTRAINT ejercicio_pkey PRIMARY KEY (id);


--
-- Name: rutina_pkey; Type: CONSTRAINT; Schema: public; Owner: roguz_admin
--

ALTER TABLE ONLY rutina
    ADD CONSTRAINT rutina_pkey PRIMARY KEY (id);


--
-- Name: rutinas_ejercicios_pkey; Type: CONSTRAINT; Schema: public; Owner: roguz_admin
--

ALTER TABLE ONLY rutinas_ejercicios
    ADD CONSTRAINT rutinas_ejercicios_pkey PRIMARY KEY (id);


--
-- Name: rutinas_tipos_cuerpo_pkey; Type: CONSTRAINT; Schema: public; Owner: roguz_admin
--

ALTER TABLE ONLY rutinas_tipos_cuerpo
    ADD CONSTRAINT rutinas_tipos_cuerpo_pkey PRIMARY KEY (id);


--
-- Name: rutinas_usuarios_pkey; Type: CONSTRAINT; Schema: public; Owner: roguz_admin
--

ALTER TABLE ONLY rutinas_usuarios
    ADD CONSTRAINT rutinas_usuarios_pkey PRIMARY KEY (id);


--
-- Name: tipo_cuerpo_pkey; Type: CONSTRAINT; Schema: public; Owner: roguz_admin
--

ALTER TABLE ONLY tipo_cuerpo
    ADD CONSTRAINT tipo_cuerpo_pkey PRIMARY KEY (id);


--
-- Name: usuario_pkey; Type: CONSTRAINT; Schema: public; Owner: roguz_admin
--

ALTER TABLE ONLY usuario
    ADD CONSTRAINT usuario_pkey PRIMARY KEY (id);


--
-- Name: detalle_ejercicio_id_ejercicio_fkey; Type: FK CONSTRAINT; Schema: public; Owner: roguz_admin
--

ALTER TABLE ONLY detalle_ejercicio
    ADD CONSTRAINT detalle_ejercicio_id_ejercicio_fkey FOREIGN KEY (id_ejercicio) REFERENCES ejercicio(id);


--
-- Name: rutinas_ejercicios_id_ejercicio_fkey; Type: FK CONSTRAINT; Schema: public; Owner: roguz_admin
--

ALTER TABLE ONLY rutinas_ejercicios
    ADD CONSTRAINT rutinas_ejercicios_id_ejercicio_fkey FOREIGN KEY (id_ejercicio) REFERENCES ejercicio(id);


--
-- Name: rutinas_ejercicios_id_rutina_fkey; Type: FK CONSTRAINT; Schema: public; Owner: roguz_admin
--

ALTER TABLE ONLY rutinas_ejercicios
    ADD CONSTRAINT rutinas_ejercicios_id_rutina_fkey FOREIGN KEY (id_rutina) REFERENCES rutina(id);


--
-- Name: rutinas_tipos_cuerpo_id_rutina_fkey; Type: FK CONSTRAINT; Schema: public; Owner: roguz_admin
--

ALTER TABLE ONLY rutinas_tipos_cuerpo
    ADD CONSTRAINT rutinas_tipos_cuerpo_id_rutina_fkey FOREIGN KEY (id_rutina) REFERENCES rutina(id);


--
-- Name: rutinas_tipos_cuerpo_id_tipo_cuerpo_fkey; Type: FK CONSTRAINT; Schema: public; Owner: roguz_admin
--

ALTER TABLE ONLY rutinas_tipos_cuerpo
    ADD CONSTRAINT rutinas_tipos_cuerpo_id_tipo_cuerpo_fkey FOREIGN KEY (id_tipo_cuerpo) REFERENCES tipo_cuerpo(id);


--
-- Name: rutinas_usuarios_id_rutina_fkey; Type: FK CONSTRAINT; Schema: public; Owner: roguz_admin
--

ALTER TABLE ONLY rutinas_usuarios
    ADD CONSTRAINT rutinas_usuarios_id_rutina_fkey FOREIGN KEY (id_rutina) REFERENCES rutina(id);


--
-- Name: rutinas_usuarios_id_usuario_fkey; Type: FK CONSTRAINT; Schema: public; Owner: roguz_admin
--

ALTER TABLE ONLY rutinas_usuarios
    ADD CONSTRAINT rutinas_usuarios_id_usuario_fkey FOREIGN KEY (id_usuario) REFERENCES usuario(id);


--
-- Name: public; Type: ACL; Schema: -; Owner: postgres
--

REVOKE ALL ON SCHEMA public FROM PUBLIC;
REVOKE ALL ON SCHEMA public FROM postgres;
GRANT ALL ON SCHEMA public TO postgres;
GRANT ALL ON SCHEMA public TO PUBLIC;


--
-- PostgreSQL database dump complete
--

