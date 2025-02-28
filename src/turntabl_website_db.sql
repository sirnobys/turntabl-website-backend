PGDMP     4                    {            postgres    15.3    15.3 +    1           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false            2           0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false            3           0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false            4           1262    5    postgres    DATABASE     �   CREATE DATABASE postgres WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE_PROVIDER = libc LOCALE = 'English_United States.1252';
    DROP DATABASE postgres;
                postgres    false            5           0    0    DATABASE postgres    COMMENT     N   COMMENT ON DATABASE postgres IS 'default administrative connection database';
                   postgres    false    3380                        3079    16384 	   adminpack 	   EXTENSION     A   CREATE EXTENSION IF NOT EXISTS adminpack WITH SCHEMA pg_catalog;
    DROP EXTENSION adminpack;
                   false            6           0    0    EXTENSION adminpack    COMMENT     M   COMMENT ON EXTENSION adminpack IS 'administrative functions for PostgreSQL';
                        false    2            �            1259    24576    website_admin    TABLE     �   CREATE TABLE public.website_admin (
    id bigint NOT NULL,
    name character varying(100) NOT NULL,
    email character varying(100) NOT NULL,
    date_created timestamp with time zone DEFAULT CURRENT_TIMESTAMP NOT NULL
);
 !   DROP TABLE public.website_admin;
       public         heap    postgres    false            �            1259    24580    admin_id_seq    SEQUENCE     u   CREATE SEQUENCE public.admin_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 #   DROP SEQUENCE public.admin_id_seq;
       public          postgres    false    227            7           0    0    admin_id_seq    SEQUENCE OWNED BY     E   ALTER SEQUENCE public.admin_id_seq OWNED BY public.website_admin.id;
          public          postgres    false    228            �            1259    16401    blogs    TABLE     �   CREATE TABLE public.blogs (
    id bigint NOT NULL,
    name character varying(100) NOT NULL,
    description text NOT NULL,
    image bytea NOT NULL,
    link json NOT NULL,
    date_created timestamp with time zone DEFAULT CURRENT_TIMESTAMP NOT NULL
);
    DROP TABLE public.blogs;
       public         heap    postgres    false            �            1259    16407    blogs_id_seq    SEQUENCE     u   CREATE SEQUENCE public.blogs_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 #   DROP SEQUENCE public.blogs_id_seq;
       public          postgres    false    215            8           0    0    blogs_id_seq    SEQUENCE OWNED BY     =   ALTER SEQUENCE public.blogs_id_seq OWNED BY public.blogs.id;
          public          postgres    false    216            �            1259    16408    career_applicants    TABLE     Q  CREATE TABLE public.career_applicants (
    id bigint NOT NULL,
    career_id integer NOT NULL,
    first_name character varying(100) NOT NULL,
    last_name character varying(100) NOT NULL,
    email character varying(100) NOT NULL,
    cv bytea NOT NULL,
    date_created timestamp with time zone DEFAULT CURRENT_TIMESTAMP NOT NULL
);
 %   DROP TABLE public.career_applicants;
       public         heap    postgres    false            �            1259    16414    career_applicants_id_seq    SEQUENCE     �   CREATE SEQUENCE public.career_applicants_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 /   DROP SEQUENCE public.career_applicants_id_seq;
       public          postgres    false    217            9           0    0    career_applicants_id_seq    SEQUENCE OWNED BY     U   ALTER SEQUENCE public.career_applicants_id_seq OWNED BY public.career_applicants.id;
          public          postgres    false    218            �            1259    16415    careers    TABLE     �  CREATE TABLE public.careers (
    id bigint NOT NULL,
    name character varying(100) NOT NULL,
    department character varying(100) NOT NULL,
    description text NOT NULL,
    requirements character varying(500)[] NOT NULL,
    responsibilities character varying(500)[] NOT NULL,
    technologies character varying(300)[] NOT NULL,
    salary character varying(50),
    date_created timestamp with time zone DEFAULT CURRENT_TIMESTAMP NOT NULL,
    hidden boolean NOT NULL
);
    DROP TABLE public.careers;
       public         heap    postgres    false            �            1259    16421    careers_id_seq    SEQUENCE     w   CREATE SEQUENCE public.careers_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 %   DROP SEQUENCE public.careers_id_seq;
       public          postgres    false    219            :           0    0    careers_id_seq    SEQUENCE OWNED BY     A   ALTER SEQUENCE public.careers_id_seq OWNED BY public.careers.id;
          public          postgres    false    220            �            1259    16422    contact    TABLE     '  CREATE TABLE public.contact (
    id bigint NOT NULL,
    name character varying(100) NOT NULL,
    email character varying(100) NOT NULL,
    company character varying(100) NOT NULL,
    description text NOT NULL,
    date_created timestamp with time zone DEFAULT CURRENT_TIMESTAMP NOT NULL
);
    DROP TABLE public.contact;
       public         heap    postgres    false            �            1259    16428    contact_id_seq    SEQUENCE     w   CREATE SEQUENCE public.contact_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 %   DROP SEQUENCE public.contact_id_seq;
       public          postgres    false    221            ;           0    0    contact_id_seq    SEQUENCE OWNED BY     A   ALTER SEQUENCE public.contact_id_seq OWNED BY public.contact.id;
          public          postgres    false    222            �            1259    16429    events    TABLE     "  CREATE TABLE public.events (
    id bigint NOT NULL,
    name character varying(100) NOT NULL,
    description text NOT NULL,
    image bytea NOT NULL,
    link json,
    status character varying(50) NOT NULL,
    date_created timestamp with time zone DEFAULT CURRENT_TIMESTAMP NOT NULL
);
    DROP TABLE public.events;
       public         heap    postgres    false            �            1259    16435    events_id_seq    SEQUENCE     v   CREATE SEQUENCE public.events_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 $   DROP SEQUENCE public.events_id_seq;
       public          postgres    false    223            <           0    0    events_id_seq    SEQUENCE OWNED BY     ?   ALTER SEQUENCE public.events_id_seq OWNED BY public.events.id;
          public          postgres    false    224            �            1259    16436    newsletters    TABLE     �   CREATE TABLE public.newsletters (
    id bigint NOT NULL,
    email character varying(100) NOT NULL,
    date_created timestamp with time zone DEFAULT CURRENT_TIMESTAMP NOT NULL
);
    DROP TABLE public.newsletters;
       public         heap    postgres    false            �            1259    16440    newsletters_id_seq    SEQUENCE     {   CREATE SEQUENCE public.newsletters_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 )   DROP SEQUENCE public.newsletters_id_seq;
       public          postgres    false    225            =           0    0    newsletters_id_seq    SEQUENCE OWNED BY     I   ALTER SEQUENCE public.newsletters_id_seq OWNED BY public.newsletters.id;
          public          postgres    false    226            �           2604    24581    blogs id    DEFAULT     d   ALTER TABLE ONLY public.blogs ALTER COLUMN id SET DEFAULT nextval('public.blogs_id_seq'::regclass);
 7   ALTER TABLE public.blogs ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    216    215            �           2604    24582    career_applicants id    DEFAULT     |   ALTER TABLE ONLY public.career_applicants ALTER COLUMN id SET DEFAULT nextval('public.career_applicants_id_seq'::regclass);
 C   ALTER TABLE public.career_applicants ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    218    217            �           2604    24583 
   careers id    DEFAULT     h   ALTER TABLE ONLY public.careers ALTER COLUMN id SET DEFAULT nextval('public.careers_id_seq'::regclass);
 9   ALTER TABLE public.careers ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    220    219            �           2604    24584 
   contact id    DEFAULT     h   ALTER TABLE ONLY public.contact ALTER COLUMN id SET DEFAULT nextval('public.contact_id_seq'::regclass);
 9   ALTER TABLE public.contact ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    222    221            �           2604    24585 	   events id    DEFAULT     f   ALTER TABLE ONLY public.events ALTER COLUMN id SET DEFAULT nextval('public.events_id_seq'::regclass);
 8   ALTER TABLE public.events ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    224    223            �           2604    24586    newsletters id    DEFAULT     p   ALTER TABLE ONLY public.newsletters ALTER COLUMN id SET DEFAULT nextval('public.newsletters_id_seq'::regclass);
 =   ALTER TABLE public.newsletters ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    226    225            �           2604    24587    website_admin id    DEFAULT     l   ALTER TABLE ONLY public.website_admin ALTER COLUMN id SET DEFAULT nextval('public.admin_id_seq'::regclass);
 ?   ALTER TABLE public.website_admin ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    228    227            �           2606    24589    website_admin admin_pkey 
   CONSTRAINT     V   ALTER TABLE ONLY public.website_admin
    ADD CONSTRAINT admin_pkey PRIMARY KEY (id);
 B   ALTER TABLE ONLY public.website_admin DROP CONSTRAINT admin_pkey;
       public            postgres    false    227            �           2606    16448    blogs blogs_pkey 
   CONSTRAINT     N   ALTER TABLE ONLY public.blogs
    ADD CONSTRAINT blogs_pkey PRIMARY KEY (id);
 :   ALTER TABLE ONLY public.blogs DROP CONSTRAINT blogs_pkey;
       public            postgres    false    215            �           2606    16450 (   career_applicants career_applicants_pkey 
   CONSTRAINT     f   ALTER TABLE ONLY public.career_applicants
    ADD CONSTRAINT career_applicants_pkey PRIMARY KEY (id);
 R   ALTER TABLE ONLY public.career_applicants DROP CONSTRAINT career_applicants_pkey;
       public            postgres    false    217            �           2606    16452    careers careers_pkey 
   CONSTRAINT     R   ALTER TABLE ONLY public.careers
    ADD CONSTRAINT careers_pkey PRIMARY KEY (id);
 >   ALTER TABLE ONLY public.careers DROP CONSTRAINT careers_pkey;
       public            postgres    false    219            �           2606    16454    contact contact_pkey 
   CONSTRAINT     R   ALTER TABLE ONLY public.contact
    ADD CONSTRAINT contact_pkey PRIMARY KEY (id);
 >   ALTER TABLE ONLY public.contact DROP CONSTRAINT contact_pkey;
       public            postgres    false    221            �           2606    16456    events events_pkey 
   CONSTRAINT     P   ALTER TABLE ONLY public.events
    ADD CONSTRAINT events_pkey PRIMARY KEY (id);
 <   ALTER TABLE ONLY public.events DROP CONSTRAINT events_pkey;
       public            postgres    false    223            �           2606    16458    newsletters newsletters_pkey 
   CONSTRAINT     Z   ALTER TABLE ONLY public.newsletters
    ADD CONSTRAINT newsletters_pkey PRIMARY KEY (id);
 F   ALTER TABLE ONLY public.newsletters DROP CONSTRAINT newsletters_pkey;
       public            postgres    false    225            �           2606    16459     career_applicants career_id_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.career_applicants
    ADD CONSTRAINT career_id_fkey FOREIGN KEY (career_id) REFERENCES public.careers(id) NOT VALID;
 J   ALTER TABLE ONLY public.career_applicants DROP CONSTRAINT career_id_fkey;
       public          postgres    false    3223    219    217           