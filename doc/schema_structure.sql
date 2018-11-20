--
-- PostgreSQL database dump
--

-- Dumped from database version 9.5.14
-- Dumped by pg_dump version 10.3

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_with_oids = false;

--
-- Name: collection_title; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.collection_title (
    id integer NOT NULL,
    title_id character varying(16) NOT NULL,
    ordering integer NOT NULL,
    title character varying(512) NOT NULL,
    region character varying(8),
    language character varying(16),
    types character varying(32),
    attributes character varying(256),
    description text,
    is_original_title boolean NOT NULL
);


ALTER TABLE public.collection_title OWNER TO postgres;

--
-- Name: collection_title_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.collection_title_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.collection_title_id_seq OWNER TO postgres;

--
-- Name: collection_title_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.collection_title_id_seq OWNED BY public.collection_title.id;


--
-- Name: collection_title id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.collection_title ALTER COLUMN id SET DEFAULT nextval('public.collection_title_id_seq'::regclass);


--
-- Name: collection_title collection_title_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.collection_title
    ADD CONSTRAINT collection_title_pkey PRIMARY KEY (id);


--
-- PostgreSQL database dump complete
--

