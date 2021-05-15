# CFD 347 Final Project
## John Steinman, Wilson Watson, Nischal Shrestha, Antonio Esquivel

In this final project, we investigate the well-known taylor couette flow. This is the flow of a viscous, incompressible fluid between a rotating inner cylinder and a fixed outer cylinder. For relatively low Reynolds numbers this flow is laminar and steady state. As the Reynolds number increases past a critical value, a second steady state is reached called vortex flow, named for the presence of Taylor vortices. As the Reynolds number continues to increase, the flow becomes periodic in a configuration called way vortex flow. 

We have written a blockMeshDict generator to facilitate the creation of meshes with variable resolution. First, we will converge the flow on finer and finer meshes. Then we will examine the flow at different Reynolds numbers, verifying the theoretical background.
