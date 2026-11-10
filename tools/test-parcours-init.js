// Propre au vocabulaire, lancé par tools/test-parcours.mjs dans un navigateur neuf (jamais sur ta vraie progression) :
// coupe les rappels surprise de la bulle い/な/て, qui cacheraient les boutons pendant le test.
try { if (!localStorage.getItem('nv-memo-v1')) localStorage.setItem('nv-memo-v1', '{"freq":"jamais"}'); } catch { /* ignore */ }
