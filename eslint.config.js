export default [
  {
    files: ["auth-ui-kit/*.js"],
    languageOptions: {
      ecmaVersion: 2021,
      sourceType: 'module',
      globals: {
        document: 'readonly',
        window: 'readonly'
      }
    },
    rules: {}
  }
];
