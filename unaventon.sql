-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 24-06-2022 a las 22:15:58
-- Versión del servidor: 10.4.24-MariaDB
-- Versión de PHP: 8.1.6

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `unaventon`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `datos_usuario`
--

CREATE TABLE `datos_usuario` (
  `correo` varchar(80) COLLATE utf8mb4_unicode_ci NOT NULL,
  `password` varchar(80) COLLATE utf8mb4_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `ircampuscarro`
--

CREATE TABLE `ircampuscarro` (
  `lat` varchar(25) COLLATE utf8mb4_unicode_ci NOT NULL,
  `lon` varchar(25) COLLATE utf8mb4_unicode_ci NOT NULL,
  `Nombre` varchar(20) COLLATE utf8mb4_unicode_ci NOT NULL,
  `celular` varchar(10) COLLATE utf8mb4_unicode_ci NOT NULL,
  `placa` varchar(6) COLLATE utf8mb4_unicode_ci NOT NULL,
  `tarifa` varchar(5) COLLATE utf8mb4_unicode_ci NOT NULL,
  `horario` varchar(10) COLLATE utf8mb4_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `datos_usuario`
--
ALTER TABLE `datos_usuario`
  ADD UNIQUE KEY `correo` (`correo`);

--
-- Indices de la tabla `ircampuscarro`
--
ALTER TABLE `ircampuscarro`
  ADD UNIQUE KEY `celular` (`celular`),
  ADD UNIQUE KEY `placa` (`placa`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
