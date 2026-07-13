fig = px.bar(
    x=category_counts.index,
    y=category_counts.values,
    title="Product Count by Category",
    labels={
        "x": "Category",
        "y": "Number of Products"
    },
    text=category_counts.values
)

fig.update_layout(
    xaxis_title="Category",
    yaxis_title="Number of Products",
    title_x=0.5
)

fig.show()
