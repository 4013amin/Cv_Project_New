/** @type {import('tailwindcss').Config} */
module.exports = {
    content: ['./app/templates/**/*.{html,js}'],
    theme: {
        extend: {
            keyframes: {
                search: {
                    'from': {transform: 'translateX(50px); opacity: 0;'},
                    'to': {transform: 'translateX(0px); opacity: 1;'},
                },
                menu: {
                    '0%, 100%': {opacity: '1;'},
                    '50%': {opacity: '.5;'}
                }
            },
            animation: {
                search: 'search .5s ease-in-out',
                menu: 'menu 1s cubic-bezier(0.4, 0, 0.6, 1) infinite'
            },
            fontFamily: {
                "Rokh-Light": "Rokh Light",
                "Rokh-Med": "Rokh Medium",
                "Rokh-Bold": "Rokh Bold",
                "IRSans-Light": "IRSans Light",
                "IRSans-Medium": "IRSans Medium",
                "IRSans-Bold": "IRSans Bold"
            },
            colors: {
                "BlueC": {
                    800: "#04A5E5",
                    300: "#C8EBF8",
                    100: "#CAF1FF"
                },
                "greenPrice": {
                    800: "#1E8F0B"
                },
                "grayPro": {800: "#747474"}
            },
            container: {
                center: true,
                padding: {
                    DEFAULT: "2rem",
                    lg: "4rem"
                }
            },
            backgroundImage: {
                'header-pattern': "url('/static/Pic/headerpattern.svg')",
            },
        },
    },
    plugins: [],
}
