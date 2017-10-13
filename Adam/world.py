import vincent
geo_data = [{'name': 'countries',
             'url': 'https://github.com/wrobstory/vincent_map_data/blob/master/world-countries.topo.json',
             'feature': 'world-countries'}]

vis = vincent.Map(geo_data=geo_data, scale=200)
vis.to_json('vega.json', html_out=True, html_path='vega_template.html')
vis.display()
