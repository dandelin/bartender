$(function() {
    $.ajax({
        type: 'POST',
        url: '/api/recipes',
        contentType: false,
        cache: false,
        processData: false,
        async: true,
        success: function(data) {
            console.log(data);
            drawtable(data);
        },
        error: function(jqXHR, textStatus, errorThrown) {
            alert(textStatus + ", " + errorThrown);
        },
        complete: function() {
        }
    });
});

function drawtable(data){
    var cocktails = d3.select('#recipes')
        .selectAll('div')
        .data(data)
        .enter()
        .append('div')
        .attr('class', function(d){return d.name;});

    cocktails.each(function(d){
        //d3.select(this).append('img')
        //    .attr('src', function(d){return "/static/" + d.img_src;});

        d3.select(this).append('p')
            .attr('class', 'cocktail-name')
            .text(function(d){return d.name;});
        
        for(var key in d.descs){
            var value = d.descs[key];
            var descs_sector = d3.select(this).append('div')
                .attr('class', 'cocktail-desc-sector');
            descs_sector.append('span')
                .attr('class', 'cocktail-label')
                .text(key);
            descs_sector.append('span')
                .attr('class', 'cocktail-desc')
                .text(value);
        }
    })
}