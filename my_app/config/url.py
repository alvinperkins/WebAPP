
pre_fix = 'todo.'

urls = (

    '/o/introduce','todo.todo.Me',
    '/o/code/dir','code.dir.random_walk',
    '/o/code/search','code.dir.search', 
    '/o/code/(.+)','code.code.CodePad',

    
    '/topic/(.+)','todo.topic.Topic',
    '/o/pandas/(.+)','andas.main.introduction',
    '/backsub','data.BackSub.search',
    
    '/o/todo',pre_fix+'todo.Index',
    '/todo/new',pre_fix+'todo.New',
     '/todo/edit',pre_fix+'todo.Edit',
    '/todo/view',pre_fix+'todo.View',
    '/count','todo.session.count',
 
    '/o/imagenet/', 'todo.image.ImageNet',
    '/o/imagenet', 'todo.image.ImageNet',

   
    '/o/','todo.todo.welcome',    
    '/o/map/(.+)',"todo.static_map.api",
    #--------------------------------------------
    
    '/comment/testnode/(.+)', 'cluster.single.TestNode',
    '/comment/trait', 'cluster.single.TraitLink',
    '/comment', 'cluster.comment',
    '/(.+)' ,   'todo.todo.default',
    '/','todo.todo.welcome'
)
