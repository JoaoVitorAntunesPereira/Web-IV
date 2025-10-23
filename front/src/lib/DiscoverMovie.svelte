<script>
	import { onMount } from "svelte";
	import MovieCard from "./MovieCard.svelte";

	let results = null;
	let year = "2025";
	let popularity = "desc";
	let genres = [];
	let selectedGenre = "";
	let title = ""
	let endpoint

	async function getDiscoverMovie() {

		if (title){
			endpoint = `http://localhost:8000/movies/search?title=${title}&release_year=${year}`
		}else{
			endpoint = `http://localhost:8000/discover/movie?release_year=${year}&popularity=${popularity}&genres=${selectedGenre}`;
		}

		console.log(endpoint);

		const res = await fetch(endpoint);
		const data = await res.json();
		results = data;

		if (res.ok) {
			return data;
		} else {
			throw new Error(data);
		}
	}

	async function handleSubmit(event) {
		event.preventDefault();
		await getDiscoverMovie();
	}

	async function getGenres() {
		let endpoint = `http://localhost:8000/genres`;

		const res = await fetch(endpoint);
		const data = await res.json();

		if (res.ok) {
			genres = data;
		} else {
			console.error(data);
		}
	}

	onMount(() => {
		getGenres();
		getDiscoverMovie();
	});
</script>

<h2>Buscar filmes</h2>

<form on:submit|preventDefault={handleSubmit}>
	<label for="title">Título</label>
	<input type="text" name="title" id="title" bind:value={title}>

	<label for="year">Ano de lançamento</label>
	<input id="year" type="text" bind:value={year} />

	<fieldset>
		<legend>Popularidade</legend>

		<label>
			<input
				type="radio"
				bind:group={popularity}
				value="asc"
				on:change={handleSubmit}
			/>
			Crescente
		</label>

		<label>
			<input
				type="radio"
				bind:group={popularity}
				value="desc"
				on:change={handleSubmit}
			/>
			Decrescente
		</label>
	</fieldset>

	<label for="genre">Gênero</label>
	<select id="genre" bind:value={selectedGenre} on:change={handleSubmit}>
		<option value="">Todos</option>
		{#each genres as genre}
			<option value={genre.id}>{genre.name}</option>
		{/each}
	</select>

	<button type="submit">Buscar</button>
</form>

{#if results}
	<h3>Resultados</h3>
	{#each results as item}
		<MovieCard {item} />
	{/each}
{/if}
