"""fix: delete owner_id workspace-model

Revision ID: 2e495c85a5ec
Revises: e7244e6c78e4
Create Date: 2022-04-26 20:38:29.993565

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2e495c85a5ec'
down_revision = 'e7244e6c78e4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('workspaces', 'owner_id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('workspaces', sa.Column('owner_id', sa.INTEGER(), autoincrement=False, nullable=False))
    # ### end Alembic commands ###