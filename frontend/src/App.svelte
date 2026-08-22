<script lang="ts">
	import Home from './lib/Home.svelte'
	import Why from './lib/Why.svelte'
	import How from './lib/How.svelte'
	let page: string = $state('home'); // keeps track of the current page

	function checkHome() {
		const currentURL = String(window.location.pathname);
		const currentPage = currentURL.slice(currentURL.indexOf('/') + 1, );
		if (currentPage !== '') page = currentPage;
		else page = 'home'; // if it says nothing after the last '/', we are at the home page.
	}

	function updatePage(event: MouseEvent & { currentTarget: EventTarget & HTMLButtonElement}, name: string) {
		event.preventDefault();
		if (name !== 'home') history.pushState(null, "", name); // the last param controls what's displayed after the / in the URL. I prefer there not being a magpie.ishu.foo/home page, but rather only magpie.ishu.foo, that's the reason for this conditional.
		else history.pushState(null, "", "/"); // forward slash == website root.
		page = name;
	}

	// also check the URL on startup (after reloads) so that we know if we are on the home page or not
	checkHome();
</script>

<svelte:window onpopstate={checkHome} />
<!-- FIXME: the dots when applied here look a bit off. Might I want a header component? -->
<nav class="md:flex flex-row justify-center items-center p-0.5 gap-100 mt-5 text-center">	
	<button class="font-mono font-bold hover:text-emerald-500 cursor-pointer transition-colors" onclick={(event) => updatePage(event, 'why')}>[ WHY? ]</button>
	<button class="font-mono font-bold hover:text-emerald-500 cursor-pointer transition-colors" onclick={(event) => updatePage(event, 'home')}>[ HOME ]</button>
	<button class="font-mono font-bold hover:text-emerald-500 cursor-pointer transition-colors" onclick={(event) => updatePage(event, 'how')}>[ HOW? ]</button>
</nav>
{#if page === 'home'}
	<Home />
{:else if page === 'why'}
	<Why />
{:else if page === 'how'}
	<How />
{/if}

<footer class="mt-10 ml-4 mb-4 text-center">
 <p>A cosmognaut production.</p>
</footer>
