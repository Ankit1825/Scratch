cd /themes/custom
mkdir my_custom_theme
cd my_custom_theme
name: 'My Custom Theme'
type: theme
description: 'A custom Drupal 10 theme using Twig and TailwindCSS.'
core_version_requirement: ^10
base theme: stable
package: Custom
libraries:
  - my_custom_theme/global-styling
regions:
  top_banner: 'Top Banner'
  logo: 'Logo'
  navigation_menu: 'Navigation Menu'
  left_sidebar: 'Left Sidebar'
  content: 'Content'
  footer: 'Footer'
global-styling:
  css:
    theme:
      css/style.css: {}
  js:
    js/script.js: {}
  dependencies:
    - core/jquery
    - core/drupal
<?php

use Drupal\Core\Template\Attribute;

/**
 * Implements hook_preprocess_HOOK() for page.html.twig.
 */
function my_custom_theme_preprocess_page(array &$variables) {
  // Add a body class if needed
  $variables['attributes']['class'][] = 'my-custom-theme';
}
<!DOCTYPE html>
<html lang="{{ language }}">
<head>
  <head-placeholder token="{{ head_placeholder_token }}">
  <title>{{ head_title }}</title>
  <css-placeholder token="{{ placeholder_token }}">
  <js-placeholder token="{{ placeholder_token }}">
</head>
<body{{ attributes }}>
  <header>
    <div class="region-top-banner">{{ page.top_banner }}</div>
    <div class="region-logo">{{ page.logo }}</div>
    <nav class="region-navigation">{{ page.navigation_menu }}</nav>
  </header>

  <main>
    <aside class="region-left-sidebar">{{ page.left_sidebar }}</aside>
    <section class="region-content">{{ page.content }}</section>
  </main>

  <footer class="region-footer">{{ page.footer }}</footer>
</body>
</html>
body {
  font-family: Arial, sans-serif;
}

.region-top-banner {
  background: #222;
  color: white;
  text-align: center;
  padding: 10px;
}

.region-logo {
  text-align: center;
  font-size: 24px;
  font-weight: bold;
}

.region-navigation {
  background: #333;
  padding: 10px;
}

.region-left-sidebar {
  width: 25%;
  float: left;
}

.region-content {
  width: 75%;
  float: right;
}

.region-footer {
  background: #222;
  color: white;
  text-align: center;
  padding: 10px;
  clear: both;
}
drush theme:enable my_custom_theme
drush config:set system.theme default my_custom_theme -y
