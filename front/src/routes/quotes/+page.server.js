/** @type {import('./$types').PageServerLoad} */
export async function load({ params }) {
	const url = "https://zenquotes.io/api/random";
  const res = await fetch(url);
  const data = res.json();
  if (res.ok) {
    return {
      zenquote: data,
    };
  } else {
    throw new Error(data);
  }
}

// import json from '$lib/data.json';
// /** @type {import('./$types').PageServerLoad} */
// export async function load({ params }) {
//   const data = json.quotes;
//   const i = Math.floor(Math.random()*json.quotes.length)
//   return {
//     zenquote: [data[i]],
//   };
// }