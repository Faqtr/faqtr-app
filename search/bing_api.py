import requests

BASE_URL = "https://api.cognitive.microsoft.com/bing/v7.0/search"
headers = {'Ocp-Apim-Subscription-Key': 'cd18b9463d45418fa44af0837b59cb51'}


def search(text):
    response = requests.get(BASE_URL, params={'q': text}, headers=headers).json()
    result_list = response['webPages']['value']
    relevant_sentence_list = []

    # Fetch various opinions and results from the search
    for res in result_list:
        snippet_parts = res['snippet'].split(". ")
        for snip in snippet_parts:

            # Eliminate ..., noise from sentence
            if len(snip.strip()) > 4:
                relevant_sentence_list.append(snip.encode('utf-8'))

    return relevant_sentence_list


# def search_cached():
#     return ['The American public estimates that 23% of Americans are gay or lesbian, little changed from the 25% estimate in 2011', 'they do not represent the only way to estimate the percentage of the population that is gay or lesbian', 'Still, all available estimates of the actual gay and lesbian population in the U.S', 'are far lower than what the public estimates, ...', 'LGBT demographics of the United States LGBT adult percentage by state in 2012', 'The ..', 'An earlier report published in April 2011 by the Williams Institute estimated that 3.8 percent of Americans identified as gay/lesbian, bisexual, or transgender: 1.7 percent as lesbian or gay ..', '(in alphabetical order), metropolitan areas, and states with the highest population of gay residents and the highest percentage of gay residents (GLB population as a percentage of total residents based on ...', 'What percentage of the U.S', 'population is gay, lesbian or bisexual? The inside track on Washington politics', 'Be the first to know about new stories from PowerPost', 'Sign up to follow, ..', 'More specifically, 1.8 percent of men self-identify as gay and 0.4 percent as bisexual, and 1.5 percent of women self-identify as lesbian and 0.9 percent as bisexual.', 'maybe two-thirds of the public will guess that America is at least 20 percent gay', 'And don\xe2\x80\x99t forget, it\xe2\x80\x99s in the interest of gay-rights activists to promote (or at least not contradict) the assumption that gays are more numerous than they are', 'The bigger the gay population seems, ..', 'John Sexton Sep 30, ...', 'Gay Population Statistics in the United States How Many Gay People Are There? Share Pin ..', 'estimates that 9 million (about 3.8%) of Americans identify as gay, lesbian, bisexual or transgender (2011)', 'The institute also found that bisexuals make up 1.8% of the population, while 1.7% are gay or lesbian', 'Transgender adults make up 0.3% of the population', 'Why is this ..', "A recent government survey found that 4 percent of adults aged 18-45 identified as 'homosexual' or ...", 'Americans Have No Idea How Few Gay People There Are', 'Most Popular', "Trump Takes to Twitter as Puerto Rico's Crisis Mounts David A", 'Graham; 2:17 PM ET ..', 'Women and young adults were most likely to provide high estimates, approximating that 30 percent of the population is gay', 'estimate that 25 percent of Americans are gay or lesbian," Gallup found.', 'In his 1948 book, Sexual Behavior in the Human Male, Alfred Kinsey shocked the world by announcing that 10% of the male population is gay', 'A 1993 Janus Report estimated that nine percent of men and five percent of women had more than "occasional" homosexual relationships', 'To some people, homosexuality is a matter of perception and definition', 'Furthermore, many people have trouble admitting their homosexuality to themselves, much less to a researcher', 'But when Gallup asked Americans for their ...', 'Data analysis suggests that roughly 5 percent of American men are gay, ..', 'Some gay men do move out of less tolerant states, but this effect is small', 'I estimate that the openly gay population would be about 0.1 percentage points higher in the least tolerant states if everyone stayed in place', 'The percent of male high school students who identify themselves as gay on Facebook is also much lower in less tolerant areas.', 'backed up by the memorable statistical claim that one in 10 of the US population was gay \xe2\x80\x93 this figure was deeply and passionately contested', 'Gay Britain: ..', 'with a much higher proportion in younger people, particularly in younger women: the percentage for women between 16 and 24 jumps nearly fourfold', 'Sexual identity is also now part of official government ..', 'gay bisexual and transgender) Americans, roughly equivalent to the population of New Jersey, according to a recent US ...', 'Demographics of sexual orientation Sexual orientation; Sexual orientations; Asexual; Bisexual ..', 'knowledge of the size of the "gay and lesbian population holds promise for helping social scientists understand a wide array of important questions ..', 'estimating based on its research that 1.7 percent of American adults identify as gay or lesbian, while another 1.8 percent identify as bisexual', 'Drawing on information from four recent national and two state-level population-based ...']
#
#
# res_list = search_cached()
# import nltk
#
#
# text = nltk.Text("30% of Americans are gay")
# for res in res_list:
#     print text.__sizeof__()
#
