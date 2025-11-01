<script>
    import { onMount } from "svelte";
    import PersonCard from "./PersonCard.svelte";

    let results = $state(null);
    let endpoint;
    let name = $state(null);
    let id = $state(null);
    let list = $state(false);

    async function getPerson() {
        if(id){
            endpoint = `http://localhost:8000/person/${id}`;
            list = false;
        }else if(name){
            endpoint = `http://localhost:8000/person/name/${name}`;
            list = true;
        }else{
            endpoint = `http://localhost:8000/trending/person/week/1`;
            list = true;
        }

        const res = await fetch(endpoint);
        const data = await res.json();
        results = data;

        if(res.ok){
            console.log(data);
            return data;
        }else{
            throw new Error(data);
        }
    }

	async function handleSubmit(event){
		await getPerson();
	}

    onMount(() => {
        getPerson();
    });

</script>

<form onsubmit={handleSubmit}>
  <label for="id">ID</label>
  <input id="id" type="text" name="id" bind:value={id} placeholder="Digite o ID" />

  <label for="name">Nome</label>
  <input id="name" type="text" name="name" bind:value={name} placeholder="Digite o nome" />

  <button type="submit">Enviar</button>
</form>

<div class="results">
    {#if results}
        {#if list}
            {#each results as item}
                <PersonCard {item}/>
            {/each}
        {:else}
            <PersonCard item = {results}/>
        {/if}
    {/if}
</div>

<style>
  form {
    max-width: 400px;
    margin: 2rem auto;
    padding: 1.5rem;
    background: #1e1e1e;
    border-radius: 12px;
    box-shadow: 0 4px 10px rgba(0, 0, 0, 0.4);
    color: #f0f0f0;
  }

  label {
    display: block;
    font-size: 0.9rem;
    margin-bottom: 0.4rem;
  }

  input {
    width: 100%;
    padding: 0.6rem;
    margin-bottom: 1rem;
    border: 1px solid #333;
    border-radius: 8px;
    background: #2a2a2a;
    color: white;
    outline: none;
    transition: border-color 0.2s, box-shadow 0.2s;
  }

  input:focus {
    border-color: #3b82f6;
    box-shadow: 0 0 0 3px rgba(59, 130, 246, 0.3);
  }

  button {
    width: 100%;
    padding: 0.7rem;
    background: #3b82f6;
    border: none;
    border-radius: 8px;
    color: white;
    font-weight: 600;
    cursor: pointer;
    transition: background 0.2s;
  }

  button:hover {
    background: #2563eb;
  }
</style>
