# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.4.1] - 2021-10-09

### Added

- Added file for image constants routes
- Added default image when missing library or image path

### Changed

- Image assets imports are now in a constants file
- Resource manager now use constants imports
- Preload separated in different functions for future updates

### Fixed

- Fixed version numbers and some dates

## [0.4.1] - 2021-10-09

### Changed

- Moved level files to own folder

### Fixed

- Added missing information from previous changes

## [0.3.1] - 2021-10-09

## Added

- requirements file for dependencies

## [0.3.0] - 2021-09-26

### Added

- Added resource manager
- The game manager now use the resource manager to get assets
- All images are now loaded in advance
- Added some assets as a proof of working resource managing

### Changed

- Moved game constants to their own folder

## [0.2.0] - 2021-09-26

### Added

- Added font initialization
- Added screen fill in every level to prevent caching old frames
- Added a text in every level for clarity

### Changed

- Renamed WIN to SCREEN as it's more readable
- Now game manager use the game screen as parameter
- Screen flip and update toggled

## [0.1.0] - 2021-09-26

### Added

- Added this Changelog!
