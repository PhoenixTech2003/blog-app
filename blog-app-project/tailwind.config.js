/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ['./blog_app/templates/blog_app/**/*.html'],
  theme: {
    extend: {
      backgroundImage: {
        'hero-image': "url('images/bible.jpg')",
        'footer-texture': "url('/img/footer-texture.png')",
      }
    },
  },
  plugins: [],
}

