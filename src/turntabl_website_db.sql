--
-- PostgreSQL database dump
--

-- Dumped from database version 15.3
-- Dumped by pg_dump version 15.3

-- Started on 2023-07-07 23:35:46 GMT

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

DROP DATABASE postgres;
--
-- TOC entry 3637 (class 1262 OID 5)
-- Name: postgres; Type: DATABASE; Schema: -; Owner: postgres
--

CREATE DATABASE postgres WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE_PROVIDER = libc LOCALE = 'C';


ALTER DATABASE postgres OWNER TO postgres;

\connect postgres

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- TOC entry 3638 (class 0 OID 0)
-- Dependencies: 3637
-- Name: DATABASE postgres; Type: COMMENT; Schema: -; Owner: postgres
--

COMMENT ON DATABASE postgres IS 'default administrative connection database';


--
-- TOC entry 2 (class 3079 OID 16384)
-- Name: adminpack; Type: EXTENSION; Schema: -; Owner: -
--

CREATE EXTENSION IF NOT EXISTS adminpack WITH SCHEMA pg_catalog;


--
-- TOC entry 3639 (class 0 OID 0)
-- Dependencies: 2
-- Name: EXTENSION adminpack; Type: COMMENT; Schema: -; Owner:
--

COMMENT ON EXTENSION adminpack IS 'administrative functions for PostgreSQL';


SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- TOC entry 224 (class 1259 OID 16785)
-- Name: blogs; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.blogs (
    id bigint NOT NULL,
    name character varying(100) NOT NULL,
    description character varying(300) NOT NULL,
    image bytea NOT NULL,
    link json NOT NULL,
    date_created timestamp with time zone DEFAULT CURRENT_TIMESTAMP NOT NULL
);


ALTER TABLE public.blogs OWNER TO postgres;

--
-- TOC entry 223 (class 1259 OID 16784)
-- Name: blogs_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.blogs_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.blogs_id_seq OWNER TO postgres;

--
-- TOC entry 3640 (class 0 OID 0)
-- Dependencies: 223
-- Name: blogs_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.blogs_id_seq OWNED BY public.blogs.id;


--
-- TOC entry 220 (class 1259 OID 16562)
-- Name: career_applicants; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.career_applicants (
    id bigint NOT NULL,
    career_id integer NOT NULL,
    first_name character varying(100) NOT NULL,
    last_name character varying(100) NOT NULL,
    email character varying(100) NOT NULL,
    cv bytea NOT NULL,
    date_created timestamp with time zone DEFAULT CURRENT_TIMESTAMP NOT NULL
);


ALTER TABLE public.career_applicants OWNER TO postgres;

--
-- TOC entry 219 (class 1259 OID 16561)
-- Name: career_applicants_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.career_applicants_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.career_applicants_id_seq OWNER TO postgres;

--
-- TOC entry 3641 (class 0 OID 0)
-- Dependencies: 219
-- Name: career_applicants_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.career_applicants_id_seq OWNED BY public.career_applicants.id;


--
-- TOC entry 218 (class 1259 OID 16540)
-- Name: careers; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.careers (
    id bigint NOT NULL,
    name character varying(100) NOT NULL,
    department character varying(100) NOT NULL,
    description character varying(500) NOT NULL,
    requirements character varying(500)[] NOT NULL,
    responsibilities character varying(500)[] NOT NULL,
    technologies character varying(300)[] NOT NULL,
    salary character varying(50),
    date_created timestamp with time zone DEFAULT CURRENT_TIMESTAMP NOT NULL
);


ALTER TABLE public.careers OWNER TO postgres;

--
-- TOC entry 217 (class 1259 OID 16539)
-- Name: careers_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.careers_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.careers_id_seq OWNER TO postgres;

--
-- TOC entry 3642 (class 0 OID 0)
-- Dependencies: 217
-- Name: careers_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.careers_id_seq OWNED BY public.careers.id;


--
-- TOC entry 226 (class 1259 OID 16796)
-- Name: contact; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.contact (
    id bigint NOT NULL,
    name character varying(100) NOT NULL,
    email character varying(100) NOT NULL,
    company character varying(100) NOT NULL,
    description character varying(500) NOT NULL,
    date_created timestamp with time zone DEFAULT CURRENT_TIMESTAMP NOT NULL
);


ALTER TABLE public.contact OWNER TO postgres;

--
-- TOC entry 225 (class 1259 OID 16795)
-- Name: contact_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.contact_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.contact_id_seq OWNER TO postgres;

--
-- TOC entry 3643 (class 0 OID 0)
-- Dependencies: 225
-- Name: contact_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.contact_id_seq OWNED BY public.contact.id;


--
-- TOC entry 222 (class 1259 OID 16759)
-- Name: events; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.events (
    id bigint NOT NULL,
    name character varying(100) NOT NULL,
    description character varying(300) NOT NULL,
    image bytea NOT NULL,
    link json,
    status character varying(50) NOT NULL,
    date_created timestamp with time zone DEFAULT CURRENT_TIMESTAMP NOT NULL
);


ALTER TABLE public.events OWNER TO postgres;

--
-- TOC entry 221 (class 1259 OID 16758)
-- Name: events_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.events_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.events_id_seq OWNER TO postgres;

--
-- TOC entry 3644 (class 0 OID 0)
-- Dependencies: 221
-- Name: events_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.events_id_seq OWNED BY public.events.id;


--
-- TOC entry 216 (class 1259 OID 16425)
-- Name: newsletters; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.newsletters (
    id bigint NOT NULL,
    email character varying(100) NOT NULL,
    date_created timestamp with time zone DEFAULT CURRENT_TIMESTAMP NOT NULL
);


ALTER TABLE public.newsletters OWNER TO postgres;

--
-- TOC entry 215 (class 1259 OID 16424)
-- Name: newsletters_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.newsletters_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.newsletters_id_seq OWNER TO postgres;

--
-- TOC entry 3645 (class 0 OID 0)
-- Dependencies: 215
-- Name: newsletters_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.newsletters_id_seq OWNED BY public.newsletters.id;


--
-- TOC entry 3473 (class 2604 OID 16788)
-- Name: blogs id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.blogs ALTER COLUMN id SET DEFAULT nextval('public.blogs_id_seq'::regclass);


--
-- TOC entry 3469 (class 2604 OID 16565)
-- Name: career_applicants id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.career_applicants ALTER COLUMN id SET DEFAULT nextval('public.career_applicants_id_seq'::regclass);


--
-- TOC entry 3467 (class 2604 OID 16543)
-- Name: careers id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.careers ALTER COLUMN id SET DEFAULT nextval('public.careers_id_seq'::regclass);


--
-- TOC entry 3475 (class 2604 OID 16799)
-- Name: contact id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.contact ALTER COLUMN id SET DEFAULT nextval('public.contact_id_seq'::regclass);


--
-- TOC entry 3471 (class 2604 OID 16762)
-- Name: events id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.events ALTER COLUMN id SET DEFAULT nextval('public.events_id_seq'::regclass);


--
-- TOC entry 3465 (class 2604 OID 16428)
-- Name: newsletters id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.newsletters ALTER COLUMN id SET DEFAULT nextval('public.newsletters_id_seq'::regclass);


--
-- TOC entry 3486 (class 2606 OID 16793)
-- Name: blogs blogs_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.blogs
    ADD CONSTRAINT blogs_pkey PRIMARY KEY (id);


--
-- TOC entry 3482 (class 2606 OID 16569)
-- Name: career_applicants career_applicants_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.career_applicants
    ADD CONSTRAINT career_applicants_pkey PRIMARY KEY (id);


--
-- TOC entry 3480 (class 2606 OID 16547)
-- Name: careers careers_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.careers
    ADD CONSTRAINT careers_pkey PRIMARY KEY (id);


--
-- TOC entry 3488 (class 2606 OID 16804)
-- Name: contact contact_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.contact
    ADD CONSTRAINT contact_pkey PRIMARY KEY (id);


--
-- TOC entry 3484 (class 2606 OID 16767)
-- Name: events events_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.events
    ADD CONSTRAINT events_pkey PRIMARY KEY (id);


--
-- TOC entry 3478 (class 2606 OID 16432)
-- Name: newsletters newsletters_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.newsletters
    ADD CONSTRAINT newsletters_pkey PRIMARY KEY (id);


--
-- TOC entry 3489 (class 2606 OID 16570)
-- Name: career_applicants career_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.career_applicants
    ADD CONSTRAINT career_id_fkey FOREIGN KEY (career_id) REFERENCES public.careers(id) NOT VALID;


-- Completed on 2023-07-07 23:35:46 GMT

--
-- PostgreSQL database dump complete
--

