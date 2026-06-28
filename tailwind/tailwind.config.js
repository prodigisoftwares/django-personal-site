module.exports = {
  content: [
    "../personal/apps/**/templates/**/*.{html,py,js}",
    "../personal/**/templates/**/*.{html,py,js}",
    "../personal/static/**/*.js",
  ],
  theme: {
    extend: {
      colors: {
        brand: {
          DEFAULT: "#4f46e5", // indigo-600
          hover: "#4338ca",   // indigo-700
        },
        surface: "#ffffff",
        success: {
          DEFAULT: "#059669", // emerald-600
          subtle: "#d1fae5",  // emerald-100
          bg: "#ecfdf5",      // emerald-50
          border: "#a7f3d0",  // emerald-200
          text: "#065f46",    // emerald-800
          muted: "#047857",   // emerald-700
        },
      },
    },
  },
};
