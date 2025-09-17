<script>
    import { onMount } from "svelte";
    import PersonCard from "$lib/PersonCard.svelte";

    let results = $state(null);

    async function getPerson() {
        let endpoint = `http://localhost:8000/trending/person/week/1`;
        const res = await fetch(endpoint);
        const data = await res.json();

        if(res.ok){
            return data;
        }else{
            throw new Error(data);
        }
    }

    getPerson().then((data) => {
        results = data;
    })

    onMount(() => {
        getPerson();
    })

</script>

<div class="results">
    {#if results}
        {#each results as item}
            <PersonCard {item}/>
        {/each}
    {/if}
</div>


