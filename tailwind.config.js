/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./src/**/*.{js,jsx,ts,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        'primary-blue': 'var(--primary-blue)',
        'orange-accent': 'var(--orange-accent)',
        'cta-orange': 'var(--cta-orange)',
        'text-dark': 'var(--text-dark)',
      },
      typography: {
        DEFAULT: {
          css: {
            color: 'var(--text-dark)',
            h1: {
              color: 'var(--primary-blue)',
            },
            h2: {
              color: 'var(--primary-blue)',
            },
            h3: {
              color: 'var(--primary-blue)',
            },
            strong: {
              color: 'var(--text-dark)',
            },
            a: {
              color: 'var(--cta-orange)',
              '&:hover': {
                color: 'var(--orange-accent)',
              },
            },
          },
        },
      },
    },
  },
  plugins: [
    require('@tailwindcss/forms'),
  ],
}
